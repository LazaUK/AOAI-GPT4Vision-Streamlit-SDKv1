# GPT-4 Turbo with Vision: Out-of-Stock Detection (Demo Solution)
GPT-4 Turbo with Vision is a multimodal Generative AI model, available for deployment in the Azure OpenAI service. It can process images and text as prompts and generate relevant textual responses to questions about them.

In this repo, you will find the source code of a Streamlit Web app that analyses shelf images of a fictitious retail shop to detect potential out-of-stock situations. The Web app can run locally on your computer and requires access to your Azure OpenAI endpoint to interact with the GPT-4 Turbo with Vision model.

To build this demo, I used the latest OpenAI Python SDK v1.x. To upgrade your _openai_ Python package, please use the following pip command:
```
pip install --upgrade openai
```

## Table of contents:
- [Part 1: Configuring solution environment](https://github.com/LazaUK/AOAI-GPT4Vision-Streamlit-SDKv1/tree/main?tab=readme-ov-file#part-1-configuring-solution-environment)
- [Part 2: Web app - User Guide](https://github.com/LazaUK/AOAI-GPT4Vision-Streamlit-SDKv1/tree/main?tab=readme-ov-file#part-2-web-app---user-guide)
- [Part 3: Web app - Developer Guide](https://github.com/LazaUK/AOAI-GPT4Vision-Streamlit-SDKv1/tree/main?tab=readme-ov-file#part-3-web-app---developer-guide)
- [Part 4: Web app - SysAdmin Guide](https://github.com/LazaUK/AOAI-GPT4Vision-Streamlit-SDKv1/tree/main?tab=readme-ov-file#part-4-web-app---sysadmin-guide)

## Part 1: Configuring solution environment
1. To use API key authentication, assign API endpoint name, version and key, along with the Azure OpenAI deployment name to **OPENAI_API_BASE**, **OPENAI_API_VERSION**, **OPENAI_API_KEY** and **OPENAI_API_DEPLOY_VISION** environment variables respectively.
![screenshot_1.1_environment](images/part1_environment.png)
>**Note**: If you want to use Entra ID (former Azure Active Directory) authentication instead, you may find some implementation options [here](https://github.com/LazaUK/AOAI-EntraIDAuth-SDKv1).
2. Install required Python packages, by using pip command and provided requirements.txt file.
```
pip install -r requirements.txt
```

## Part 2: Web app - User Guide
1. To launch the Web app, you should run the following command from this repo's root folder
```
streamlit run GPT4V_Streamlit.py
```
2. If everything was installed correctly as per the Part 1's instructions above, you should be able to access demo solution's Web page at http://localhost:8501 locally.
![screenshot_2.2_environment](images/part2_mainui.png)
3. The UI is very minimalistic. You need to click one of the Web cam buttons, first, to display simulated shelf image of fictitious retail shop.
4. Then you can click Analyse button to submit selected image to your GPT-4 Turbo with Vision model in Azure OpenAI. If no significant gaps, then the model should reply with a simple "Ok". If the model will detect a potential out-of-stock situation because of the wider gap, then it should reply with a more verbose answer, describing location and specifics of its findings.
>**Note**: As a Generative AI solution, GPT-4 Turbo with Vision is not deterministic. So, you may get slightly different descriptions of the same image if analysed several time and it's expected.

## Part 3: Web app - Developer Guide
1. This Web app is based on Streamlit, an open source Python framework and doesn't require explicit setup of a Web service or programming in any other languages.
2. **image_paths** dictionary contains button names for mock Web cams and associated JPEG images of the shop shelves. If you want to use your own images, just update relevant references.
``` Python
image_paths = {
    "Web cam # 1": "images/GPT4V_OutOfStock_Image1.jpg",
    "Web cam # 2": "images/GPT4V_OutOfStock_Image2.jpg",
    "Web cam # 3": "images/GPT4V_OutOfStock_Image3.jpg",
    "Web cam # 4": "images/GPT4V_OutOfStock_Image4.jpg"
}
```
3. Connection with the backend Azure OpenAI service is established through _openai_ Python SDK v1. Current implementation passes Azure OpenAI endpoint's API key as a parameter value of AzureOpenAI class. If necessary, you can switch to the Entra ID authentication instead.
``` Python
client = AzureOpenAI(
    azure_endpoint = AOAI_API_BASE,
    api_key = AOAI_API_KEY,
    api_version = AOAI_API_VERSION
)
```
4.  As test images are hosted locally, they are converted into Base64 strings - one of the supported GPT-4 Turbo with Vision's input formats. 
``` Python
with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")
```
5.  Base64 string is then passed as a part of the user prompt. Alternatively, you can enter here URLs of remotely hosted images.
``` Python
{ 
    "type": "image_url",
    "image_url": {
        "url": f"data:image/jpeg;base64,{base64_image}"
    }
}
```
6.  As an "easter egg", the Web app will animate snow flakes on the first run or after Web browser session's refresh. Post-festive season, you can comment out line # 35.
``` Python
st.snow() # New Year's theme :)
```

## Part 4: Web app - SysAdmin Guide
1. This repo comes with an attached Docker image on GitHub Container Registry (GHCR), which has a pre-built environment with all the required dependencies. It allows you to launch the Web app as a container without getting deep into its code specific.
2. There
  - Pull
```
docker pull ghcr.io/lazauk/gpt4v-outofstock:latest
```
  - Then

```
docker run -p 8501:8501 --env OPENAI_API_BASE --env OPENAI_API_DEPLOY_VISION --env OPENAI_API_KEY --env OPENAI_API_VERSION ghcr.io/lazauk/gpt4v-outofstock:latest
```
