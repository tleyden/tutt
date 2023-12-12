from enum import Enum
import re
import json 
import os
import constants

class CategoriesStorage():
    def __init__(self, categories_filename: str = "categories.json"):
        # Load in the categories from the categories.json file
        with open(os.path.join(constants.PROJECT_ROOT, categories_filename)) as f:
            self.categories_db = json.load(f)

    def find_category_for_index(self, index: int) -> str:
        for category in self.categories_db["categories"]:
            if category["index"] == index:
                return category["name"]
        return constants.CATEGORY_UNKNOWN