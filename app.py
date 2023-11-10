from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="ENCARNACION's Webpage", page_icon=":blush:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return none
    return r.json()

# CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles/style.css")

#----LOADING ASSETS
lottie_cat = load_lottieurl("https://lottie.host/47fbc972-3274-4c3a-b224-9e5d5ba06b91/hY3jjgb2oL.json")
img_IF_I_HAD_ONE = Image.open("images/if-i-had-one-angry.gif")
#----HEADER SECTION
with st.container():
    st.subheader("TESTING TESTING HI HELLO")
    st.title("ENCARNACION'S BLOG")
    st.write("THIS IS A BLOG FROM ENCARNACION THAT USES STREAMLIT AND PYTHON FOR THEIR CODING CLASS")
    st.write("[GITHUB LINK](https://github.com/BlackCat-055/STREAMLIT_PYTHON_BLOG.com)")

# ABOUT ME
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                Hi Hello Hi This is Blog for Computer Programming Class, Look at all these funny letters wooooooo
                :blush: :blush: :smile: :wave: :car: :car:
                - TEst
                - Woot
                - Lorem Ipsum
                """
            )
    with right_column:
        st_lottie(lottie_cat, height=300, key="Cat")

# ------ PROJECTOOOOS
with st.container():
    st.write("-----")
    st.header("My Projects")
    st.write("###")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_IF_I_HAD_ONE)
    with text_column:
        st.subheader("SOMETHING SOMETHING A SOON TO BE PROJECTO")
        st.write(
            """
            This is where I would put my eventual Python Project for Programming class IF I HAD ONE!!!!!
            """
        )

with st.container():
    text_column  , image_column = st.columns((2,1))
    with text_column:
        st.subheader("SOMETHING SOMETHING A SOON TO BE PROJECTO")
        st.write(
            """
            ALSO ANOTHER PLACE WHERE I COULD HAVE A PROJECT IF I HAD ONE!!!!!
            """
        )
    with image_column:
        st.image(img_IF_I_HAD_ONE)

# -------------CONTACT------------------
with st.container():
    st.write("----")
    st.header("CONTACT INFO")
    st.write("#####")
    # DOCUMENTATION
    contact_form ="""
    <form action="https://formsubmit.co/jencarnacion@ssct.edu.ph" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Weezotron-30000" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="SEND THINE WRIT OF SURVEY TO THINE!!!!" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()