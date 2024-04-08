import streamlit as st
from PIL import Image

def main():
    st.title('Image Uploader')

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Get image details
        image_info = get_image_info(uploaded_file)
        st.write("Image Details:")
        st.write(image_info)

def get_image_info(uploaded_file):
    image = Image.open(uploaded_file)
    size = image.size
    img_format = image.format
    mode = image.mode
    return {"Size": size, "Format": img_format, "Mode": mode}

if __name__ == "__main__":
    main()
