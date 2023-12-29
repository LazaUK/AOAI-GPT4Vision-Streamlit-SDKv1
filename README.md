# GPT-4 Turbo with Vision: Out-of-Stock Detection Demo Solution
Using Azure OpenAI deployment of GPT-4-Turbo with Vision to analyse out-of-stock situation in a fictitious shop.

... 

Version 1106 of Azure OpenAI GPT models, such as GPT-35-Turbo and GPT-4-Turbo, now supports the use of parallel function calling. This new feature allows your Azure OpenAI based solution to extract multiple intents from a single prompt, check the functions available and then execute them in parallel. As a result, your solution will perform more effectively and efficiently because of fewer round-trips between required multiple API calls.

In this repo I'll demo the use of the latest *openai* Python package v1.x, that was released in November 2023. To upgrade your *openai* python package, please use the following pip command:
```
pip install --upgrade openai
```

## Table of contents:
- [Part 1: Configuring Streamlit Web app]()
- [Part 2: Web app - User Guide]()
- [Part 3: Web app - Developer Guide]()

## Part 1: Configuring Streamlit Web app
1. Add a new environment variable named **FLASK_APP** that points to the provided *Vehicle_API_Simulations.py* Python script.
![screenshot_1.1_environment](images/step1_flask_env.png)
2. Install required Python packages, by using pip command and provided requirements.txt file.
```
pip install -r requirements.txt
```

## Part 2: Web app - User Guide
## Part 3: Web app - Developer Guide
