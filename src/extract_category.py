
from enum import Enum
import re
from categories_storage import CategoriesStorage
import constants


def extract_category_llm_response(llm_response: str, categories_storage: CategoriesStorage) -> str:
    """
    Extract the category from the LLm response
    """
    
    # Look for string with Category #X, where X is a number with up to 3 digits
    pattern = r'Category #\d{1,3}'

    result = re.finditer(pattern, llm_response, re.MULTILINE)
    for match in result:
        category_str = match.group(0)
        category_num = int(category_str.split("#")[1])
        return categories_storage.find_category_for_index(category_num)

    return constants.CATEGORY_UNKNOWN


def test_extract_category():

    categories_storage_test = CategoriesStorage(categories_filename="categories_example.json")

    test_cases = [
        ("KetoApp", 'Category #2 - Employment at KetoApp\n\nThe screenshot shows a coding environment where a script is being run that involves taking screenshots and possibly categorizing them. This aligns with the description of TUTT, which is developing a time tracker app that uses computer vision and language models to categorize content captured from user screens. The code seems to involve actions such as "Grabbing screenshot," "Invoke OpenAI," and dealing with data categorized in a dataset folder, which are consistent with the tasks described for TUTT\'s time tracker application development.'),
        ("Acme_AI", 'The category this screenshot most likely relates to is:\n\nCategory #1 - Employment at Acme AI\n\nThe screenshot appears to be from a company\'s internal messaging platform, specifically from a channel labeled "#engineering" within the interface of the company Arcee AI. In the messages, individuals are discussing elements related to cloud computing services, costs, and technical aspects of machine learning models (mention of DALMs - domain-specific adapted large language models). Moreover, there is mention of AWS services, which fits well with Arcee AI\'s description of deploying models on various platforms including AWS. There is also technical lingo that suggests conversations about model training and infrastructure, which aligns with the description of Arcee AI\'s operations. The overall context and content of the screenshot are far more technical and specifically related to employment at a tech company than they are to leisure activities or a time tracker app as described in the other categories.'),
        ("Leisure", 'Category #3 - Leisure, not work related.\n\nThe screenshot shows a user browsing Airbnb, which is a platform commonly used for booking vacation rentals and experiences. This activity is typically associated with personal leisure rather than work-related tasks. None of the job-related activities or companies listed in Category #1 (Arcee AI) or Category #2 (TUTT, The Ultimate Time Tracker) match the content of the screenshot. Searching for unique accommodations on Airbnb aligns more with leisure activities such as planning a vacation or looking for places to stay during personal travel, which fits into Category #3 as described in the post.')
    ]
    for expected_output, test_input in test_cases:
        actual_output = extract_category_llm_response(
            llm_response=test_input,
            categories_storage=categories_storage_test
        )
        assert actual_output == expected_output, f"Expected {expected_output}, got {actual_output}"
    print(f"All {len(test_cases)} tests passed!")


def main():
    test_extract_category()

if __name__ == "__main__":
    main()