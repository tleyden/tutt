TUTT (The Ultimate Time Tracker) is a prototype time tracker that uses the OpenAI Vision and your prompt engineering skills to accurately categorize what you're doing on your computer.

It takes a snaphot of your screen every 5 minutes and sends it (along with your prompt) to the OpenAI Vision API to find the category, then it saves it in a local database along with the screenshot.  The web UI displays your recent categorized work.

<screenshots>

**Caveats**

* Cost is approximately $1/day with the default settings
* Since your screenshots are being sent to OpenAI, **there are a lot of security and privacy risks with this app, only use it if you understand those risks**.  Note that the data is not sent anywhere else besides OpenAI.

## System requirements 

Anywhere that can run python and node.js

## Customize for your use case

### Create a custom prompt

```
cp prompt_example.txt prompt.txt
```

and customize `prompt.txt` to fit your use case.  

The categories listed in the prompt must be formatted with category numbers, as is done in the example prompt:

```
Category #1 - Employment at Acme AI

... 

Category #2 - Employment at side project: KetoMeals App 
```

You can add as many categories as you want, but these category ids need to match the `category_id` fields in the `categories.json` file that you will create in the next step.

It's recommended to spend some time designing your prompt!  You will get much more accurate results if your prompt is good.

### Create custom categories that match prompt

```
cp categories_example.json categories.json
```

Add the categories you mentioned in your custom prompt.

## Launch tutt screen grabber

Tutt consistests of two components:

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

## TODO

- add screenshots to readme
- test on a clean box
- share private repo with friends to test the instructions
- share with the internet
