import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Oriol Faus Portfolio",
    page_icon="📊",
)


def home_page():
    # ----- Left menu -----
    with st.sidebar:
        st.image("eae_img.png", width=200)
        st.header("Introduction to Programming Languages for Data")
        st.write("###")
        st.write("***Final Project - Dec 2025***")
        st.write("**Author:** Oriol Faus Galtés")
        st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


    # ----- Top title -----
    st.html("""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Oriol</h1></div>""")


    # ----- Profile image file -----
    profile_image_file_path = "profile.jpeg"

    with open(profile_image_file_path, "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


    # ----- Your Profile Image -----
    st.html(f"""
    <div style="display: flex; justify-content: center;">
        <img src="{img}" alt="Oriol Faus Galtés" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    </div>
    """)


    # ----- Personal title or short description -----
    current_role = "Software developer<br>Student of MSc: Big data and Analytics"

    st.html(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""")

    st.write("##")    # Adding some space


    # ----- About me section -----
    st.subheader("About Me")

    st.write("""
    - 🧑‍💻 I am a Software developer at Adiquímica S.A
             
    - 🛩️ Bachelor's degree in Bioinformatics (ESCI UPF)

    - ❤️ Passionate about sports, specially football, and music!

    - 🤖 Don't have any personal projects at the moment.

    - 🏂 Football, cycling, running, music, concerts, ...

    - 📫 How to reach me: ofausg@student.eae.es

    - 🏠 Barcelona
    """)

    # Feel free to add other points like your Linkedin, Github, Social Media, etc.


# This is ensambling the entire app with the different pages and the navigation menu
pg = st.navigation([
    st.Page(home_page, title="Home", icon="👋"),
    st.Page("pages/01_image_cropper.py", title="Image Cropper", icon="🖼️"),
    st.Page("pages/02_netflix_data_analysis.py", title="Netflix Data Analysis", icon="🎬"),
    st.Page("pages/03_temperatures_dashboard.py", title="Temperatures Dashboard", icon="🌦️"),
])
pg.run()