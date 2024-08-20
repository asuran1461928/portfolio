import streamlit as st
from PIL import Image
import json

# Load data from JSON files
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Load images
profile_image = Image.open('assets/profile.jpg')

# Load JSON data
education = load_json('data/education.json')
experience = load_json('data/experience.json')
projects = load_json('data/projects.json')
publications = load_json('data/publications.json')

# Header
st.image(profile_image, width=150)
st.title("Karthikeya Tallapaneni")
st.subheader("BE-CSE (Hons.) - AI and Machine Learning")

# Introduction
st.write("I am a BE-CSE(Hons.) student specializing in AI and Machine Learning at Chandigarh University in collaboration with IBM. "
         "My passion for creating scalable software solutions drives my eagerness to contribute to DevOps and cybersecurity projects.")

# Contact Information
st.write("📞 Phone: (+91) 8978796351")
st.write("📍 Location: Kandukur, Andhra Pradesh")
st.write("📧 Email: karthikeyaa.official@gmail.com")
st.write("[GitHub](https://github.com/asuran1461928) | [LinkedIn](https://www.linkedin.com/in/karthikeya-a195a121a/)")

# Skills
st.header("Skills")
st.write("**Tools and Languages:** Python, C, C++, Java, JavaScript, SQL, Data Structures, Algorithms, Shell Script, Bash, Docker, Kubernetes, GCP, React.js, Node.js, Cybersecurity Tools, Django, Flask, TensorFlow, PyTorch, OpenCV.")
st.write("**Technologies:** Machine Learning, Deep Learning, AI, NLP, Computer Vision, Data Analysis, Data Visualization, Full Stack Development, DevOps, Cybersecurity.")

# Education
st.header("Education")
for edu in education:
    st.subheader(edu['degree'])
    st.write(f"{edu['institution']} ({edu['year']})")
    st.write(f"**CGPA:** {edu['cgpa']}")

# Experience
st.header("Experience")
for exp in experience:
    st.subheader(exp['role'])
    st.write(f"{exp['company']} ({exp['year']})")
    st.write(exp['description'])

# Projects
st.header("Projects")
for proj in projects:
    st.subheader(proj['title'])
    st.write(proj['description'])

# Publications
st.header("Research Publications")
for pub in publications:
    st.subheader(pub['title'])
    st.write(pub['abstract'])
    st.write(f"[Read more]({pub['doi']})")

# Certifications
st.header("Certifications")
st.write("**Computer Vision Fundamentals with Google Cloud:** [Link](https://coursera.org/share/5d7ef2dce7ec297e1b42cb7d95e2fe9b)")
st.write("**Production Machine Learning Systems:** [Link](https://coursera.org/share/a2785a144f10045fdf4f4b32bd9fb1f9)")
st.write("**Recommendation Systems on Google Cloud:** [Link](https://coursera.org/share/2ebe6643de2685ff9deb19258dd0efe9)")

# Activities
st.header("Activities")
st.write("NASA Space App Challenge 2023")
st.write("Google Development Hackathon 2023")
st.write("Hack the Box Competition 2022")

# Footer
st.write("© 2024 Karthikeya Tallapaneni")
