import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

# Constants
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
DEFAULT_IMAGE = "./zebra.jpg"

# ... existing code ...

def convert_image(img: Image.Image) -> bytes:
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def fix_image(upload: str | BytesIO) -> None:
    try:
        col1, col2 = st.columns(2)
        image = Image.open(upload)
        col1.write("Original Image :camera:")
        col1.image(image)
        
        fixed = remove(image)
        col2.write("Fixed Image :wrench:")
        col2.image(fixed)
        
        st.sidebar.markdown("\n")
        st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")
    except Exception as e:
        st.error(f"An error occurred while processing the image: {str(e)}")

# ... existing code ...
st.title("Background Remover")
my_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image(DEFAULT_IMAGE)