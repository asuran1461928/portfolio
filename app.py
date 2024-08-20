

import streamlit as st
import json
import os

# Function to load JSON data
def load_json(file_name):
    if not os.path.exists(file_name):
        st.error(f"File not found: {file_name}")
        return []
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        st.error(f"Error reading JSON file {file_name}: {e}")
        return []

# Load JSON data
projects = load_json('projects.json')
publications = load_json('publications.json')

# Display the photo
image_path = 'Photo.png'
if os.path.exists(image_path):
    st.image(image_path, caption='Karthikeya Tallapaneni', use_column_width=True)
else:
    st.error(f"Image not found: {image_path}")

# Portfolio title
st.title("Karthikeya Tallapaneni - Portfolio")

# About Section
st.header("About Me")
st.write("""
I am Karthikeya Tallapaneni, a BE-CSE(Hons.) student specializing in AI and Machine Learning at Chandigarh University in collaboration with IBM. 
With strong skills in C, ASP.Net, SQL Server, and JavaScript frameworks like React.js, my passion for creating scalable and impactful software 
solutions fuels my eagerness to contribute to DevOps and cybersecurity projects. I thrive in Agile environments and have hands-on experience 
with CI/CD processes, cloud technologies, and developing data pipelines. My solid foundation in system architecture, object-oriented design, 
and design patterns has equipped me with a comprehensive understanding of both software development and operational efficiencies. I am excited 
about the opportunity to apply my skills to real-world DevOps and cybersecurity challenges, aiming to enhance system reliability, security, 
and performance.
""")

# Projects Section
st.header("Projects")
for project in projects:
    st.subheader(project['title'])
    st.write(f"**Date:** {project['date']}")
    st.write(project['description'])

# Publications Section
st.header("Publications")
for publication in publications:
    st.subheader(publication['title'])
    st.write(f"**Abstract:** {publication['abstract']}")
    st.write(f"[DOI]({publication['doi']})")

# Skills Section
st.header("Skills")
st.write("""
**Tools and Languages:** Python, C, C++, JavaScript, SQL, Java, Data Structures and Algorithms, Shell Script, Bash, VS Code, Git, GitHub, OOPs, Linux/Unix, Docker, Kubernetes, Google Cloud Platform (GCP), GKE (Google Kubernetes Engine), CloudSQL, VMs (Virtual Machines), Logging, Jenkins, ReactJS, NodeJS, Networking Concepts and Protocols, Cybersecurity Tools, Django, Flask.

**Platforms:** Tableau, Power BI, Firebase Database, Weka, Excel, Orange, Figma (UI/UX), Spark, Wireshark, Nmap, Burp Suite, Netmon, MS Excel, MS Word, MS PowerPoint, SharePoint.

**Libraries and Frameworks:** OpenCV, PyTorch, TensorFlow, Numpy, Pandas, NLTK, YOLO, Tkinter, Embedded, LangChain, Data Bricks, Airflow.

**Technologies:** Machine Learning, Deep Learning, Image Processing, Computer Vision, Natural Language Processing, Artificial Intelligence, Generative AI, Large Language Models (LLMs), Data Analysis, Data Visualization, Data Modeling, Endpoint Security, Network Security, Protocols, Cryptography, Zero Knowledge Proofs, Firewalls, VPNs, Bug Bounty, Web Application Security Threats, Exploits, Information Security, Cybersecurity, Penetration Testing, Full Stack Development, DevOps.
""")

# Contact Section
st.header("Contact")
st.write("""
- **Phone:** (+91) 8978796351
- **Location:** Kandukur, Andhra Pradesh
- **Email:** [karthikeyaa.official@gmail.com](mailto:karthikeyaa.official@gmail.com)
- **GitHub:** [github.com/asuran1461928](https://github.com/asuran1461928)
- **LinkedIn:** [linkedin.com/in/karthikeya-a195a121a/](https://linkedin.com/in/karthikeya-a195a121a/)
""")
