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

# Custom CSS for styling
st.markdown("""
    <style>
        /* General settings */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
        }
        .stApp {
            background-color: #f7f9fc;
            padding: 2rem;
            border-radius: 10px;
        }
        /* Header styling */
        .title h1 {
            font-size: 2.5rem;
            color: #0072b5;
            margin-bottom: 0.5rem;
        }
        /* Subheader styling */
        .stHeader h2 {
            font-size: 1.5rem;
            color: #004d80;
            border-bottom: 2px solid #0072b5;
            padding-bottom: 0.2rem;
        }
        /* Paragraph styling */
        .stMarkdown p {
            font-size: 1.1rem;
            line-height: 1.6;
            color: #333;
        }
        /* Column styling */
        .stColumn {
            padding: 1rem;
        }
        /* Project and publication cards */
        .card {
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .card h3 {
            font-size: 1.3rem;
            color: #00507a;
            margin-bottom: 0.5rem;
        }
        /* Contact section styling */
        .contact {
            font-size: 1.1rem;
            color: #0072b5;
            line-height: 1.6;
        }
        .contact a {
            color: #00507a;
            text-decoration: none;
        }
        /* Photo styling */
        .photo img {
            border-radius: 10px;
            border: 3px solid #0072b5;
        }
    </style>
""", unsafe_allow_html=True)

# Create two columns
col1, col2 = st.columns([2, 1])  # Adjust the ratio as needed

with col1:
    # Portfolio title
    st.markdown('<div class="title"><h1>Karthikeya Tallapaneni - Portfolio</h1></div>', unsafe_allow_html=True)
    
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
        st.markdown(f"""
        <div class="card">
            <h3>{project['title']}</h3>
            <p><strong>Date:</strong> {project['date']}</p>
            <p>{project['description']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Publications Section
    st.header("Publications")
    for publication in publications:
        st.markdown(f"""
        <div class="card">
            <h3>{publication['title']}</h3>
            <p><strong>Abstract:</strong> {publication['abstract']}</p>
            <p><a href="{publication['doi']}">DOI</a></p>
        </div>
        """, unsafe_allow_html=True)

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
    st.markdown("""
    <div class="contact">
        - **Phone:** (+91) 8978796351<br>
        - **Location:** Kandukur, Andhra Pradesh<br>
        - **Email:** <a href="mailto:karthikeyaa.official@gmail.com">karthikeyaa.official@gmail.com</a><br>
        - **GitHub:** <a href="https://github.com/asuran1461928">github.com/asuran1461928</a><br>
        - **LinkedIn:** <a href="https://linkedin.com/in/karthikeya-a195a121a/">linkedin.com/in/karthikeya-a195a121a/</a><br>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Display the photo
    image_path = 'Photo.jpg'
    if os.path.exists(image_path):
        st.markdown('<div class="photo">', unsafe_allow_html=True)
        st.image(image_path, caption='Karthikeya Tallapaneni', use_column_width=True, width=200)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error(f"Image not found: {image_path}")
