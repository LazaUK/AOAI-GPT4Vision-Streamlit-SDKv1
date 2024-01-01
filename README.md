# GPT-4 Turbo with Vision: Out-of-Stock Detection (Demo Solution)
GPT-4 Turbo with Vision is a multimodal Generative AI model, available for deployment in the Azure OpenAI service. It can process images and text as prompts and generate relevant textual responses to questions about them.

In this repo, you will find the source code of a Streamlit Web app that analyses shelf images of a fictitious retail shop to detect potential out-of-stock situations. The Web app can run locally on your computer and requires access to your Azure OpenAI endpoint to interact with the GPT-4 Turbo with Vision model.

To build this demo, I used the latest OpenAI Python SDK v1.x. To upgrade your _openai_ Python package, please use the following pip command:
```
pip install --upgrade openai
```

## Table of contents:
- [Part 1: Configuring solution environment](https://github.com/LazaUK/AOAI-GPT4Vision-Streamlit-SDKv1/tree/main#part-1-configuring-solution-environment)
- [Part 2: Web app - User Guide](https://github.com/LazaUK/AOAI-GPT4Vision-Streamlit-SDKv1/tree/main#part-2-web-app---user-guide)
- [Part 3: Web app - Developer Guide]()
- [Part 4: Web app - SysAdmin Guide]()

## Part 1: Configuring solution environment
1. To use API key authentication, assign API endpoint name, version and key, along with the Azure OpenAI deployment name to **OPENAI_API_BASE**, **OPENAI_API_VERSION**, **OPENAI_API_KEY** and **OPENAI_API_DEPLOY_VISION** environment variables.
![screenshot_1.1_environment](images/part1_environment.png)
>**Note**: If you want to use Entra ID (former Azure Active Directory) authentication instead, you may check some implementation options out [here](https://github.com/LazaUK/AOAI-EntraIDAuth-SDKv1).
2. Install required Python packages, by using pip command and provided requirements.txt file.
```
pip install -r requirements.txt
```

## Part 2: Web app - User Guide
1. To launch the Web app, you should run the following command from this repo's root folder
```
streamlit run GPT4V_Streamlit.py
```
2. If everything was installed correctly as per Part 1 instructions above, you should be able to access demo solution's Web page at http://localhost:8501 locally.
![screenshot_2.2_environment](images/part2_mainui.png)
4. 

## Part 3: Web app - Developer Guide
## Part 4: Web app - SysAdmin Guide
