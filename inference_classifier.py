import cv2
import mediapipe as mp
import numpy as np
import streamlit as st
import pickle
import base64
import pyttsx3

def load_model():
    model_dict = pickle.load(open('./model.p', 'rb'))
    return model_dict['model']

def model():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
    labels_dict = {0: 'Hello', 1: 'Peace', 2: 'OK', 3: 'No'}

    model = load_model()

    # Initialize camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Unable to open camera.")
        return

    # Create Streamlit columns
    col1, col2 = st.columns([1, 3])

    # Create a Streamlit text box in the left column
    with col1:
        st.text("Predicted Sign:")
        predicted_sign_textbox = st.empty()

    # Create a Streamlit video frame in the right column
    with col2:
        video_frame = st.empty()

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

                    # Predict gesture
                    try:
                        prediction = model.predict([np.asarray(data_aux)])
                        # After predicting the character
                        predicted_character = labels_dict[int(prediction[0])]

                        # Update text box with predicted character
                        predicted_sign_textbox.text(predicted_character)

                        # Overlay gesture on frame
                        cv2.putText(frame, predicted_character, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                        # Convert text to speech
                        engine = pyttsx3.init()
                        engine.say(predicted_character)
                        engine.runAndWait()
                    except:
                        pass

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

# Run the model function
model()
