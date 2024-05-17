import cv2
import mediapipe as mp
import numpy as np
import streamlit as st
import pickle
import base64
import pyttsx3
from googletrans import Translator
from labels_dict import labels_dict

translator = Translator()

@st.cache_data()
def load_model():
    model_dict = pickle.load(open('./model.p', 'rb'))
    return model_dict['model']

def model():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
    model = load_model()

    # Initialize camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Unable to open camera.")
        return

    # Create Streamlit columns
    col1, col2 = st.columns([3, 1])

    # Create a Streamlit text box in the left column
    with col1:
        video_frame = st.empty()

    # Create a Streamlit video frame in the right column
    with col2:
        st.text("Predicted Sign:")
        predicted_sign_textbox = st.empty()

        st.text("Translated Sign:")
        translated_sign_textbox = st.empty()

        lang = st.selectbox("Select language", ["English", "Hindi", "Marathi", "Gujarati"])

        if lang == "English":
            selected_language_code = 'en'
        elif lang == "Hindi":
            selected_language_code = 'hi'
        elif lang == "Marathi":
            selected_language_code = 'mr'
        elif lang == "Gujarati":
            selected_language_code = 'gu'

        # Apply CSS styling for video container
        st.markdown(
            """
            <style>
            .video-container {
                display: flex;
                justify-content: center;
                align-items: center;
                border: 2px solid black;
                border-radius: 10px;
                overflow: hidden;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Initialize text-to-speech engine
        engine = pyttsx3.init()

        # Variable to store the previous predicted character
        prev_predicted_character = None

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                st.error("Error: Failed to capture frame.")
                break

            # Process frame with MediaPipe hands
            results = hands.process(frame)

            # Draw hand landmarks and classify gesture
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw hand landmarks
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())

                    # Extract hand landmarks
                    data_aux = []
                    x_ = []
                    y_ = []

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y

                        x_.append(x)
                        y_.append(y)

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))

                    x1 = int(min(x_) * frame.shape[1]) - 10
                    y1 = int(min(y_) * frame.shape[0]) - 10
                    x2 = int(max(x_) * frame.shape[1]) - 10
                    y2 = int(max(y_) * frame.shape[0]) - 10

                    prediction = model.predict(
                        [np.asarray(data_aux + [0] * (84 - len(data_aux)))]
                    )
                    predicted_character = labels_dict[prediction[0]]

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                    cv2.putText(
                        frame,
                        predicted_character,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.3,
                        (150, 150, 150),
                        3,
                        cv2.LINE_AA,
                    )

                    # Translate the predicted sign
                    try:
                        translated_sign = translator.translate(predicted_character, dest=selected_language_code).text
                    except Exception as e:
                        translated_sign = "Translation Error"

                    # Convert text to speech
                    if predicted_character != prev_predicted_character:
                        engine.say(predicted_character)
                        engine.runAndWait()

                    # Update the previous predicted character
                    prev_predicted_character = predicted_character

                    # Display predicted sign and translated sign
                    predicted_sign_textbox.text(predicted_character)
                    translated_sign_textbox.text(translated_sign)

            # Convert the frame to base64 encoded string
            _, buffer = cv2.imencode('.jpg', frame)
            frame_base64 = base64.b64encode(buffer).decode('utf-8')

            # Display the resulting frame within the styled video container
            video_frame.markdown(
                f'<div class="video-container"><img src="data:image/jpeg;base64,{frame_base64}" style="max-width:100%;"></div>',
                unsafe_allow_html=True
            )

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()