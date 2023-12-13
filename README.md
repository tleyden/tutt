TUTT (The Ultimate Time Tracker) is a prototype time tracker that uses the OpenAI Vision and your prompt engineering skills to accurately categorize what you're doing on your computer.

It takes a snaphot of your screen every 5 minutes and sends it (along with your prompt) to the OpenAI Vision API to find the category, then it saves it in a local database along with the screenshot.  The web UI displays your recent categorized work.

| | |
|---|---|
|List of time tracking events | Details of time tracking event|
|  ![Screenshot 2023-12-13 at 2 00 48 PM](https://github.com/tleyden/tutt/assets/296876/6eb41f46-049e-465d-a69d-8bcb2e2f852c) |  ![Screenshot 2023-12-13 at 2 01 09 PM](https://github.com/tleyden/tutt/assets/296876/e35801c1-f283-4dca-a24e-c960f7210a3a)  |


**Caveats**

* Cost is approximately $1/day with the default settings
* Since your screenshots are being sent to OpenAI, **there are a lot of security and privacy risks with this app, only use it if you understand those risks**.  Note that the data is not sent anywhere else besides OpenAI.

## System requirements 

Any system that can run python and node.js

You will also need access to GPT-4.  According to the [OpenAI website](https://platform.openai.com/docs/guides/vision):

> GPT-4 with vision is currently available to all developers who have access to GPT-4 via the gpt-4-vision-preview model and the Chat Completions API which has been updated to support image inputs.
If you're a Pay-As-You-Go customer and you've made a successful payment of $1 or more, you'll be able to access the GPT-4 API (8k).



## Customize for your use case

### Create a custom prompt

```
cp prompt_example.txt prompt.txt
```

and customize `prompt.txt` to fit your use case.  

The categories listed in the prompt must be formatted with category numbers like `Category #<num>`, as is done in the example prompt:

```
Category #1 - <title of category 1>

... 

Category #2 - <title of category 2>
```

You can add as many categories as you want, but these category ids need to match the `category_id` fields in the `categories.json` file that you will create in the next step.

It's recommended to spend some time designing your prompt!  You will get much more accurate results if your prompt is good.

### Create custom categories that match prompt

```
cp categories_example.json categories.json
```

Add the categories you mentioned in your custom prompt.

The category ids need to match the `category_id` fields in the `categories.json` file, and the category names should be concise.


## Launch TUTT screen grabber

Tutt consists of two components:

1. A python screen grabber
2. A Vue.js web UI to view the captured screenshots with their categories

This section walks you through getting the python screen grabber running.

You can run it in the background with `tmux` or similar.

### Step 1: Create a conda env or virtualenv

```
conda create --name tutt python=3.11
conda activate tutt
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Setup environment variables (OpenAI API KEY)

You must have an OpenAI account that allows access to the [Vision API](https://platform.openai.com/docs/guides/vision).

```
export OPENAI_API_KEY=<your OPENAI API key>
```

### Step 4: Run TUTT screen grabber loop

```
python tutt.py
```

You can run it in the background with `tmux` or similar.  When your machine restarts, you will have to manually restart the script.


## Launch TUTT web UI

### Step 1: NPM install (one time only)

```
cd ui/tutt
npm install
```

### Step 2: Start server

```
./start_server.sh
```

It will display the localhost address that you can view in a browser.

