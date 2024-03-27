import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Sign Language Helper", page_icon=":raised_hand_with_fingers_splayed:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Navbar
selected = option_menu(None, ["Home", "Model", "Dictionary", "About Us"], 
                      icons=["house", "cloud-upload", "list-task", "gear"], 
                      menu_icon="cast", default_index=0, orientation="horizontal")

# Display content based on selected option
if selected == "Home":
    st.write("Welcome to the Home Page!")
    # Add your home page content here

elif selected == "Model":
    st.write("This is the Model Page!")
    # Add your model page content here

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
    # with right_column:
    #     st_lottie(lottie_coding, height=300, key="coding")
        
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
    
