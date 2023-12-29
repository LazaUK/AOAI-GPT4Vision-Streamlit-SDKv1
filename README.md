# GPT-4 Turbo with Vision: Out-of-Stock Detection (Demo Solution)
GPT-4 Turbo with Vision is a multimodal Generative AI model, available for deployment in the Azure OpenAI service. It can process images and text as prompts and generate relevant textual responses to questions about them.

In this repo, you will find the source code of a Streamlit Web app that analyses shelf images of a fictitious retail shop to detect potential out-of-stock situations. The Web app can run locally on your computer and requires access to your Azure OpenAI endpoint to interact with the GPT-4 Turbo with Vision model.

To build this demo, I used the latest OpenAI Python SDK v1.x. To upgrade your *openai* Python package, please use the following pip command:
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
