"""
Give a dataset, invoke the OpenAI API to get the LLm response, 
and then validate the response against the expected category.

This facilitates prompt engineering to improve the prompt and make
sure it doesn't cause any regressions
"""
import constants
import os
import json 
from dataset import read_dataset_entries
from llm import invoke_openai_api
from extract_category import extract_category_llm_response
import time

def validate_dataset(dataset_root: str):
    """
    For each entry in the dataset:

    - Run through LLM 
    - Get the category
    - Compare to expected category
    - Calculate accuracy
    """

    correct_classifications = 0
    total_classifications = 0    

    dataset_entries = read_dataset_entries(dataset_root=dataset_root)

    for dataset_entry in dataset_entries:
        print(dataset_entry)
        screenshot_filename = dataset_entry["screenshot_filename"]
        expected_category = dataset_entry["expected_category"]

        # Invoke the OpenAI API
        llm_response = invoke_openai_api(
            screenshot_filename=screenshot_filename,
            prompt=constants.PROMPT
        )
        print(llm_response)

        # Extract the category from the result
        category = extract_category_llm_response(llm_response)

        # Compare to expected category
        if category == expected_category:
            correct_classifications += 1
        else:
            print(f"Expected {expected_category}, got {category} for image {screenshot_filename}")

        total_classifications += 1

        # Throttle it a bit to avoid rate limiting
        print("Sleeping for 5 seconds to avoid rate limiting .. ")
        time.sleep(5)

    print(f"Final accuracy score: {float(correct_classifications)/float(total_classifications)} based on {correct_classifications} correct out of {total_classifications} total")


if __name__ == "__main__":
    project_root = constants.PROJECT_ROOT
    dataset_root = os.path.join(project_root, "dataset", "training_dataset")

    validate_dataset(dataset_root=dataset_root)