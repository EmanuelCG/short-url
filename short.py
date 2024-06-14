import pyshorteners
import pyshorteners.exceptions
import streamlit as st
import base64

def short_url(url, option):
    try:
        s = pyshorteners.Shortener()
        shrortener = getattr(s, option)
        return shrortener.short(url)
    except pyshorteners.exceptions.BadAPIResponseException:
        st.warning("API Key is required for this service")
    except Exception as e:
        st.error("API Key is required for this service")

#Web
st.set_page_config(page_title="Short URL", page_icon="🪓", layout="centered")

# Image center...
image_path = "images/undraw_link_shortener.png"
with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode()


st.markdown(
    f"""
    <div style='display: flex; justify-content: center;'>
        <img src='data:image/png;base64,{image_data}' style='width: 300px;'>
    </div>
    """,
    unsafe_allow_html=True
)
# End image center...

st.title("URL Shortener")
url = st.text_input("Enter the URL")
options = ["tinyurl", "adfly", "bitly", "chilpit", "cuttly", "gitio"]
selected_option = st.radio("Shortener options", options, horizontal=True)
if st.button("Generate new URL"):
    if url:
        st.write("URL shortened: ", short_url(url, selected_option))
    else:
        st.warning("Please enter a URL")


