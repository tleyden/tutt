import os 
import json 

def read_dataset_entries(dataset_root: str) -> list:
    """
    Read the dataset entries from the dataset file
    """

    # Open the dataset metadata file
    dataset_metadata_filename = os.path.join(dataset_root, "dataset.json")

    # Open the dataset metadata file
    with open(dataset_metadata_filename, "r") as dataset_metadata_file:
        dataset_metadata = json.load(dataset_metadata_file)

    return dataset_metadata["entries"]

def add_dataset_entry(dataset_root: str, screenshot_filename: str, category: str, llm_response: str, capture_time_formatted: str) -> None:
    """
    Add a dataset entry to the dataset file
    """

    # Open the dataset metadata file
    dataset_metadata_filename = os.path.join(dataset_root, "dataset.json")

    # Create the dataset metadata file if it doesn't exist
    if not os.path.exists(dataset_metadata_filename):
        with open(dataset_metadata_filename, "w") as dataset_metadata_file:
            json.dump({
                "entries": []
            }, dataset_metadata_file)

    # Open the dataset metadata file
    with open(dataset_metadata_filename, "r") as dataset_metadata_file:
        dataset_metadata = json.load(dataset_metadata_file)

    # Add the new entry
    dataset_metadata["entries"].append({
        "capture_time_formatted": capture_time_formatted,
        "screenshot_filename": screenshot_filename,
        "actual_category": category,
        "expected_category": category,
        "llm_response": llm_response
    })

    # Write the updated dataset metadata file
    with open(dataset_metadata_filename, "w") as dataset_metadata_file:
        json.dump(dataset_metadata, dataset_metadata_file)
