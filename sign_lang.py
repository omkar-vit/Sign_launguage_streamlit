import streamlit as st
import cv2
from streamlit_lottie import st_lottie          #pip install streamlit-lottie
import requests                                 #pip install requests 
from streamlit_option_menu import option_menu   #pip install streamlit-option-menu

st.set_page_config(page_title="Sign Language Helper", page_icon=":raised_hand_with_fingers_splayed:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
video1 = open("sign_video.mp4", "rb")  

# Navbar
selected = option_menu(None, ["Home", "Model", "Dictionary", "About Us"], 
                      icons=["house", "cloud-upload", "list-task", "gear"], 
                      menu_icon="cast", default_index=0, orientation="horizontal")

# Display content based on selected option
if selected == "Home":
    with st.container():
        st.write("Step into the world of Sign Language, where every sign tells a story and every gesture bridges worlds.:wave:")
        st.title("SignSpeak: Where silent gestures find their powerful voice.")
        st.subheader("Explore our project to witness the transformative impact of bridging communication divides and fostering inclusivity.")
        st.write("Join us as we embark on this enlightening journey together! [learn more >](https://google.com)")

    #what I do//// maybe add a video
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What we do")
            st.write("##")
            st.subheader(
        """
        Hello, I'm [Your Name]. Welcome to signSpeak!
        
        - With signSpeak, we've created a platform that understands your signs, translates them into written text, and even converts them into spoken words.
        - Record your signs using a camera or webcam, and our technology will detect and translate them into your preferred language.
        - You can also convert the translated text into spoken words, making it easier for everyone to understand.
        
        Thank you for joining us on this journey. Feel free to reach out if you have any questions or feedback.

        """
            )
            
        with right_column:
            width = 46
        #     width = st.sidebar.slider(
        #     label="Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
        # )
        #     width = max(width, 0.01)
            side = max((100 - width) / 2, 0.01)

            _, container, _ = st.columns([side, width, side])
            container.video(data=video1)

elif selected == "Model":
    cap = cv2.VideoCapture(1)
    detect = st.camera_input("")

elif selected == "Dictionary":
    st.write("Here's the Dictionary Page!")
    # Add your dictionary page content here

elif selected == "About Us":
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Inspiration about the project")
            st.write("##")
            st.write(
                """
                The Idea of our project was:
                - blablabla
                - blablabla
                - blablabla
                - blablabla

                If you got any quesiton, feel free to connect with us through email.
                """
            )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
    with st.container():
        st.write("---")
        st.header("Get In Touch With Us!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/saeeshweta1831@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
    
