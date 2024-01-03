TUTT (The Ultimate Time Tracker) is a prototype time tracker that sends screenshots to the OpenAI Vision API to categorize what you're doing on your computer.  

If you create a good prompt that describes your normal activities, the result can be quite accurate.

Here's what the web UI looks like when displaying your recently categorized activities.

| | |
|---|---|
|List of time tracking events | Details of time tracking event|
|  ![Screenshot 2023-12-13 at 2 00 48 PM](https://github.com/tleyden/tutt/assets/296876/6eb41f46-049e-465d-a69d-8bcb2e2f852c) |  ![Screenshot 2023-12-13 at 2 01 09 PM](https://github.com/tleyden/tutt/assets/296876/e35801c1-f283-4dca-a24e-c960f7210a3a)  |


## Why I created this

I need to track billable hours for freelance work, and I want a tool that requires the least amount of effort.  The best app I could find was [Timely App](https://timelyapp.com/), but I feel their auto-categorization feature isn't accurate enough for my needs and I still need to put in manual effort to categorize the hours.

## Caveats (why you shouldn't use this)

* This is just a proof of concept and is very unpolished.  But if you're interested in a polished version, smash that ⭐ icon!
* The OpenAI API costs are approximately $1/day with the default settings.  Open an issue if you are interested in support for running a Llava open source model.
* Since your screenshots are being sent to OpenAI, **there are a lot of security and privacy risks with this app**.  You should **only use it if you understand those risks**.  Note that the data is not sent anywhere else besides OpenAI.

## System requirements 

Only works on OSX, due to the [quickgrab](https://github.com/akrabat/QuickGrab/tree/update) dependency.

You will also need access to GPT-4, since at the time of writing this readme, according to the [OpenAI website](https://platform.openai.com/docs/guides/vision):

> GPT-4 with vision is currently available to all developers who have access to GPT-4 via the gpt-4-vision-preview model and the Chat Completions API which has been updated to support image inputs.
If you're a Pay-As-You-Go customer and you've made a successful payment of $1 or more, you'll be able to access the GPT-4 API (8k).


## Install prerequisite packages

### Quickgrab screenshot capture

This works on OSX only.

```
git clone https://github.com/akrabat/QuickGrab.git
cp QuickGrab/quickgrab /usr/local/bin
```

### Python3

This should already be installed, run `python --version` or `python3 --version` to double check.  If not, you can install it with `brew install python`.

### NodeJS

```
brew install node
```

It has been tested with:

* nodejs version v18.16.0
* npm version 9.5.1

## Customize TUTT for your use case (or else it won't work)

The [example prompt](prompt_example.txt) and [example categories](categories_example.json) won't give any meaningful results, so you will need to create a custom prompt and corresponding categories.  It should only take a few minutes.

### Create a custom prompt

Copy the example prompt:

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

### Create custom categories that match prompt (or else it won't work)

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


### Step 1 (optional): Create a conda env or virtualenv

To isolate your python dependencies and avoid any potential dependency conflicts, you can create and activate a virtual environment:

```
python3 -m venv tutt
source tutt/bin/activate
```

or with conda:

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
cd src
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


## Roadmap

None yet, but if you are interested in this app, give the repo a star and I will try to put some more time into building this into a usable app!  Feel free to file issues for any improvements you'd like to see.


## Related open source projects

* [REM - An open source approach to locally record and enable searching everything you view on your Apple Silicon.](https://github.com/jasonjmcghee/rem)
* [ActivityWatch - Open source time tracker](https://activitywatch.net/)