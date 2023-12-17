import base64
import requests
import os

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def invoke_openai_api(screenshot_filename, prompt) -> str:

    # OpenAI API Key
    api_key = os.environ["OPENAI_API_KEY"]

    # Path to your image
    image_path = screenshot_filename

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # maybe specify temperature?
    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": prompt
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 4096
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", 
        headers=headers, 
        json=payload
    )

    response_json = response.json()
    return response_json['choices'][0]['message']['content'] 
