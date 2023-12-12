import time 
import datetime 
import os
from extract_category import extract_category_llm_response, WorkCategory
import constants
from dataset import add_dataset_entry
from utils import find_most_recent_filename, grab_screenshot_to_timestamp_file, identical_to_latest_screenshot, image_is_blank
from llm import invoke_openai_api
from categories_storage import CategoriesStorage

"""

TUTT runs in a loop and grabs and classifiies screenshots from a fixed set of 
"what am I doing categories" like:

* Working on Acme AI
* Working on KetoApp
* Leisure, not work related

This will be used to create a dataset of screenshots that with their 
categories.

Detailed steps:

1. Grab a screenshot and save it to a file
2. Invoke the OpenAI API to classify the screenshot
3. Post-process raw LLM result to get a classification
4. Record the classification result in a JSON file (or delta lake table?)
"""

SCREENSHOT_GRAB_INTERVAL_SECONDS = 300

def grab_and_record(dataset_root: str, prompt: str, categories_storage: CategoriesStorage) -> None:

    # Get the current most recent png file in the dataset root for later comparison
    prior_most_recent_png_filename = find_most_recent_filename(dataset_root, "*.png")

    screenshot_filename_fq_path, formatted_time, _ = grab_screenshot_to_timestamp_file(
        dataset_root=dataset_root
    )

    # Is it a completely blank image?  For example, if the user focused on Authy,
    # it will be a blank image.  If so, skip it.
    if image_is_blank(screenshot_filename_fq_path):
        return 

    # Is it identical to the last screenshot taken?  If so, assume the
    # user is just sitting idle and skip it (any visual clocks will break this)
    if identical_to_latest_screenshot(screenshot_filename_fq_path, prior_most_recent_png_filename):
        print("Skipping and deleting identical screenshot")
        os.remove(screenshot_filename_fq_path)
        return

    # Invoke the openai api to get the category
    print(f"Invoke OpenAI on {screenshot_filename_fq_path}")
    llm_response = invoke_openai_api(
        screenshot_filename=screenshot_filename_fq_path,
        prompt=prompt
    )
    print(llm_response)

    # Extract the category from the result
    category = extract_category_llm_response(
        llm_response=llm_response,
        categories_storage=categories_storage
    )
    print(f"Category: {category}")

    # Slugify the category
    category_slug = category.name.lower().replace(" ", "_").replace("-", "_")

    # Rename the screenshot file to include the category
    screenshot_filename_basename = os.path.basename(screenshot_filename_fq_path)
    new_screenshot_file_basename = f"{category_slug}_{screenshot_filename_basename}"
    new_screenshot_filename = os.path.join(dataset_root, new_screenshot_file_basename)
    os.rename(screenshot_filename_fq_path, new_screenshot_filename)

    # Write the screenshot and category to the database
    add_dataset_entry(
        dataset_root=dataset_root,
        screenshot_filename=os.path.basename(new_screenshot_filename),
        category=category,
        llm_response=llm_response,
        capture_time_formatted=formatted_time,
    )



def main():

    project_root = constants.PROJECT_ROOT

    # read the prompt from the prompt.txt file
    if not os.path.exists(os.path.join(project_root, "prompt.txt")):
        print("Create your prompt.txt file in the project root by copying the prompt_example.txt file and customizing it for your use case.")
        exit(1)
    with open(os.path.join(project_root, "prompt.txt")) as f:
        prompt = f.read()
        print(f"Prompt: {prompt}")

    # Create the dataset root dir
    dataset_root = os.path.join(project_root,  "dataset")

    # Create the dataset root dir if it doesn't exist
    if not os.path.exists(dataset_root):
        os.makedirs(dataset_root)

    categories_storage = CategoriesStorage()

    # Main loop
    i = 0
    while True:
        try:

            if i == 0:
                sleep_seconds = 10
            else:
                sleep_seconds = SCREENSHOT_GRAB_INTERVAL_SECONDS
                
            wakeup_time = datetime.datetime.now() + datetime.timedelta(seconds=sleep_seconds)
            print(f"Sleeping for {sleep_seconds} seconds until {wakeup_time}")
            time.sleep(sleep_seconds)

            grab_and_record(
                dataset_root=dataset_root,
                prompt=prompt,
                categories_storage=categories_storage
            )

            i += 1
        except Exception as e:
            print(f"Error: {e}")
            print("Sleeping for 60 seconds and trying again")
            time.sleep(60)

if __name__ == "__main__":
    main()
