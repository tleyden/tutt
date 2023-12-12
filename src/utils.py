import datetime
import glob
import os
import subprocess

from PIL import Image


def grab_screenshot_to_timestamp_file(dataset_root):

    current_time = datetime.datetime.now()

    # Formatting the time as "8:13 AM" or similar format
    formatted_time = current_time.strftime("%I:%M %p")

    current_timestamp_seconds = current_time.timestamp()

    # Create a filename for the screenshot image based on the current time
    screenshot_filename_fq_path = os.path.join(dataset_root, f"{current_timestamp_seconds}.png")

    subprocess.run(["quickgrab", "-file", screenshot_filename_fq_path])

    print(f"Saved screenshot to {screenshot_filename_fq_path}")

    return screenshot_filename_fq_path, formatted_time, current_timestamp_seconds


def find_most_recent_filename(directory: str, extension: str) -> str | None:

    # Create a pattern to match files (eg, *.png)
    pattern = os.path.join(directory, extension)

    # Find all .png files in the directory
    png_files = glob.glob(pattern)

    if not png_files:
        return None

    # Find the most recently modified file
    latest_file = max(png_files, key=os.path.getmtime)

    return latest_file


def are_images_equal(image_path1, image_path2):
    # Open the images
    with Image.open(image_path1) as img1, Image.open(image_path2) as img2:
        # Check if the sizes are the same
        if img1.size != img2.size:
            return False

        # Compare pixel data
        pixels1 = list(img1.getdata())
        pixels2 = list(img2.getdata())

        return pixels1 == pixels2


def identical_to_latest_screenshot(screenshot_filename: str, prior_most_recent_png_filename: str) -> bool:

    if not prior_most_recent_png_filename:
        return False

    return are_images_equal(screenshot_filename, prior_most_recent_png_filename)


def image_is_blank(screenshot_filename: str) -> bool:
    """
    TODO: implement this
    """
    return False