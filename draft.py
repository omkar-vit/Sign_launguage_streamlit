import cv2
import streamlit as st
import numpy as np
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import requests  # pip install requests
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
from inference_classifier import model  # Ensure your model is correctly imported and usable
import mediapipe as mp  # Add this line

st.set_page_config(page_title="Sign Language Helper", page_icon=":raised_hand_with_fingers_splayed:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
video1 = open("sign_video.mp4", "rb")

# Navbar
selected = option_menu(None, ["Home", "Model", "Dictionary", "Game", "About Us"],
                       icons=["house", "cloud-upload", "list-task", "controller", "gear"],
                       menu_icon="cast", default_index=0, orientation="horizontal")

# Display content based on selected option
if selected == "Home":
    with st.container():
        st.write("Step into the world of Sign Language, where every sign tells a story and every gesture bridges worlds.:wave:")
        st.title("SignSpeak: Where silent gestures find their powerful voice.")
        st.subheader("Explore our project to witness the transformative impact of bridging communication divides and fostering inclusivity.")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What we do")
            st.write("##")
            st.subheader(
                """
                Hello, Welcome to SignSpeak!

                - With SignSpeak, we've created a platform that understands your signs, translates them into written text, and even converts them into spoken words.
                - Record your signs using a camera or webcam, and our technology will detect and translate them into your preferred language.
                - You can also convert the translated text into spoken words, making it easier for everyone to understand.

                Thank you for joining us on this journey. Feel free to reach out if you have any questions or feedback.
                """
            )
        with right_column:
            width = 50
            side = max((100 - width) / 2, 0.01)
            _, container, _ = st.columns([side, width, side])
            container.video(data=video1)

elif selected == "Model":
    col1, col2 = st.columns(2)
    cap = cv2.VideoCapture(0)
    model()

elif selected == "Dictionary":
    text = """
    Indiansignlanguage.org offers a vast collection of Indian Sign Language (ISL) signs. Each sign is accompanied by an image, a running video, and threaded discussions. It is an ideal resource for learning or teaching Indian Sign Language. We are continuously adding more signs and developing new services to empower the Deaf community.
    Please share your ideas and comments to help us improve this service."""
    video_url = "https://youtu.be/xwGHOUcnnHU?list=TLGGWlgSddFPLisyODAzMjAyNA"
    st.write("")
    st.write("")
    col1, col2 = st.columns([4, 3])
    with col1:
        st.write("##")
        st.markdown(f'<div class="text-container">{text}', unsafe_allow_html=True)
    with col2:
        st.video(video_url)
    with st.sidebar:
        option = st.selectbox(
            "Which signs you would like to see?",
            ("Alphabets (A to Z)", "Numbers (0 to 9)"),
            index=None,
            placeholder="Select one option",
        )
    if option == "Alphabets (A to Z)":
        num_columns = 5
        num_rows = 6
        columns = st.columns(num_columns)
        max_images = min(26, num_rows * num_columns)
        for img_number in range(1, max_images + 1):
            row = (img_number - 1) // num_columns
            col_index = (img_number - 1) % num_columns
            col = columns[col_index]
            with col.expander(f"Image {img_number}"):
                col.image(f"images/{img_number}.jpg", width=150)
        col_width = 100 / num_columns
        st.write(
            f"""
            <style>
            .reportview-container .main .block-container {{
                max-width: 100%;
            }}
            .reportview-container .main {{
                padding-left: 0;
                padding-right: 0;
            }}
            .reportview-container .main .block-container .block-element {{
                width: calc({col_width}% - 20px);
                display: inline-block;
                margin-right: 20px;
                margin-bottom: 20px;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
    elif option == "Numbers (0 to 9)":
        num_columns = 5
        num_rows = 2
        columns = st.columns(num_columns)
        for row in range(num_rows):
            for i, col in enumerate(columns):
                if row == 0:
                    img_number = row * num_columns + i + 30
                else:
                    img_number = (row - 1) * num_columns + i + 35
                with col.expander(f"Image {img_number}"):
                    if img_number <= 39:
                        col.image(f"images/{img_number}.jpg", width=200)
                        col.write(f"<div style='text-align: center; padding: 5px;'>{img_number - 30} </div>", unsafe_allow_html=True)
        col_width = 100 / num_columns
        st.write(
            f"""
            <style>
            .reportview-container .main .block-container {{
                max-width: 100%;
            }}
            .reportview-container .main {{
                padding-left: 0;
                padding-right: 0;
            }}
            .reportview-container .main .block-container .block-element {{
                width: calc({col_width}% - 20px);
                display: inline-block;
                margin-right: 20px;
                margin-bottom: 20px;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

elif selected == "Game":
    st.title("Sign Language Game")
    st.write("Choose a sign and try to replicate it in front of your camera. If you do it correctly, you'll win!")

    options = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    selected_option = st.selectbox("Choose a sign to practice", options)

    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        stframe.image(frame, channels="BGR")

        # Preprocess the frame and predict gesture
        preprocessed_frame = preprocess(frame)
        predicted_gesture = model.predict(preprocessed_frame)

        if predicted_gesture == selected_option:
            st.balloons()
            st.success("Congratulations! You made the correct sign!")
            break

    cap.release()

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
                - To promote inclusive communication and support sign language users.
                - To break communication barriers between the deaf community.
                - Empower users to confidently express themselves and engage with others.

                If you got any question, feel free to connect with us through email.
                """
            )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
    with st.container():
        st.write("---")
        st.header("Get In Touch With Us!")
        st.write("##")
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

