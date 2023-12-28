# Importing required packages
from openai import AzureOpenAI
import streamlit as st
import base64
import os

# Defining Web cam image details
image_paths = {
    "Web cam # 1": "images/GPT4V_OutOfStock_Image1.jpg",
    "Web cam # 2": "images/GPT4V_OutOfStock_Image2.jpg",
    "Web cam # 3": "images/GPT4V_OutOfStock_Image3.jpg",
    "Web cam # 4": "images/GPT4V_OutOfStock_Image4.jpg"
}

# Extracting environment variables
AOAI_API_BASE = os.getenv("OPENAI_API_BASE")
AOAI_API_KEY = os.getenv("OPENAI_API_KEY")
AOAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
AOAI_DEPLOYMENT = os.getenv("OPENAI_API_DEPLOY_VISION")

# Initiating Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint = AOAI_API_BASE,
    api_key = AOAI_API_KEY,
    api_version = AOAI_API_VERSION
)

# Defining various variables
base64_image = None
current_image = None
current_image_name = None
analyse_button = False
if "camera" not in st.session_state:
    st.session_state.camera = None
    st.snow() # New Year's theme :)

# Defining helper function to call Azure OpenAI endpoint using Python SDK
def gpt4v_completion(image_path):
    # Encoding image to base64
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    # Calling Azure OpenAI endpoint via Python SDK
    response = client.chat.completions.create(
        model = AOAI_DEPLOYMENT, # model = "Azure OpenAI deployment name".
        messages = [
            {"role": "system", "content": "You are a useful shop image analyser. You are checking for visible gaps on the shelves to detect out-of-stock situation. Important! When you detect gaps, you should report details of specific shellves, so that the shop staff can replenish products. Only, and crucially only when all shelves are well stocked, then you can reply with 'Ok' as a single word."},
            {"role": "user", "content": [  
                { 
                    "type": "text", 
                    "text": "Please, check this shelf image." 
                },
                { 
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]} 
        ],
        max_tokens = 500
    )
    return response.choices[0].message.content

# Creating sidebar with instructions
st.sidebar.header("Instructions:")
st.sidebar.markdown(
    """
    This app allows you to choose between 4 Web cam images to check different areas of your fictitious shop.
    When you click specific Web cam button, its image is shown on the right side of the app.
    
    
    There is also an additional button, called Analyse.
    When you click it, your selected Web cam's image is submitted to GPT-4-Turbo with Vision in your Azure OpenAI deployment to perform the image analysis and report its results back to the app.
    """
)

# Creating Home Page UI
st.title("Out-Of-Stock Shop Assistant")
main_container = st.container()
col1, col2 = main_container.columns([1, 3])
image_placeholder = col2.empty()
result_container = st.container()
result_placeholder = result_container.empty()

# Creating button for each Web cam in the first column
for image_name, image_path in image_paths.items():
    # If the cam button is clicked, load the image and display it in the second column
    if col1.button(image_name):
        image_placeholder.image(image=image_path, caption=image_name, use_column_width=True)
        current_image = image_path
        current_image_name = image_name
        st.session_state.camera = image_name
        analyse_button = False
    # If the analysis button is clicked, preserve the last selected image
    elif st.session_state.camera == image_name:
        image_placeholder.image(image=image_path, caption=image_name, use_column_width=True)
        current_image = image_path
        current_image_name = image_name
        st.session_state.camera = image_name

# Creating analysis button in the first column
if col1.button("Analyse"):
    analyse_button = True

# If the analysis button is clicked, use GPT-4V to analyse the image
if analyse_button and current_image is not None:
    my_bar = st.progress(50, text="Processing your image. Please wait...")
    result = gpt4v_completion(current_image)
    my_bar.progress(100)
    result_placeholder.text(
        f"Image analysis results for {current_image_name}:\n{result}"
    )