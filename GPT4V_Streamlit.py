# Importing required packages
import streamlit as st

# Defining Web cam image details
image_paths = {
    "Web cam # 1": "images/GPT4V_OutOfStock_Image1.jpg",
    "Web cam # 2": "images/GPT4V_OutOfStock_Image2.jpg",
    "Web cam # 3": "images/GPT4V_OutOfStock_Image3.jpg",
    "Web cam # 4": "images/GPT4V_OutOfStock_Image4.jpg"
}

# Defining various variables
current_image = None
current_image_name = None
analyse_button = False
if "camera" not in st.session_state:
    st.session_state.camera = None

# Defining image analysis function
def analyse_image(image):
    result = "No out-of-stock items detected"
    return result

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
    st.snow() # New Year's theme :)
    result = analyse_image(current_image)
    result_placeholder.text(
        f"Image analysis results for {current_image_name}:\n{result}"
    )