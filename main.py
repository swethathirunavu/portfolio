import streamlit as st
import base64
from PIL import Image
import requests
from io import BytesIO

# Configure the page
st.set_page_config(
    page_title="Swetha T - Portfolio",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .project-card {
        background: linear-gradient(145deg, #f0f2f6, #ffffff);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        border-left: 4px solid #1f77b4;
    }
    .skill-chip {
        background-color: #1f77b4;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        margin: 0.2rem;
        display: inline-block;
    }
    .contact-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
    }
    .achievement-item {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border-left: 3px solid #28a745;
    }
    .download-cv {
        background: linear-gradient(45deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: bold;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    .download-cv:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
sections = ["Home", "About", "Skills", "Projects", "Experience", "Education", "Certifications", "Contact"]
selected_section = st.sidebar.radio("Go to:", sections)

# Function to create download link for CV
def create_download_link():
    return """
    <a href="#" class="download-cv" onclick="alert('CV download feature will be implemented with actual PDF file')">
        📄 Download CV
    </a>
    """

# HOME SECTION
if selected_section == "Home":
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<h1 class="main-header">SWETHA T</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Computer Science Engineering Student | Machine Learning Enthusiast | Full-Stack Developer</p>', unsafe_allow_html=True)
        
        # Profile image placeholder
        st.image("https://via.placeholder.com/300x300/1f77b4/ffffff?text=SWETHA+T", width=300)
        
        st.markdown(create_download_link(), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("CGPA", "9.17", "Excellent")
    
    with col2:
        st.metric("Projects Completed", "3+", "Live Projects")
    
    with col3:
        st.metric("Technologies", "10+", "Proficient")
    
    with col4:
        st.metric("Leadership Roles", "5+", "Active Leader")

# ABOUT SECTION
elif selected_section == "About":
    st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        **Passionate and self-driven B.Tech Computer Science student** with strong skills in Machine Learning (ML), 
        JavaScript, HTML, CSS, Streamlit, and Python. Proficient in applying Data Structures and Algorithms (DSA) 
        to build efficient, real-world solutions.
        
        Known for developing impactful projects like smart route-finding apps and adolescent mental health prediction tools. 
        Eager to apply my skills and grow in a collaborative, innovation-focused environment.
        
        I have experience in leadership roles, having spearheaded promotional campaigns that led to a 30% increase in 
        participation and managed social media presence for tech communities. I'm also passionate about social impact, 
        having volunteered to teach digital literacy to students with zero digital access.
        """)
        
        st.markdown("### What I Do")
        st.write("🤖 **Machine Learning & AI**: Building predictive models with high accuracy")
        st.write("🌐 **Full-Stack Development**: Creating interactive web applications")
        st.write("📊 **Data Analysis**: Extracting insights from complex datasets")
        st.write("👥 **Leadership & Community**: Leading tech communities and mentoring others")
    
    with col2:
        st.markdown(create_download_link(), unsafe_allow_html=True)
        
        st.markdown("### Quick Facts")
        st.info("📍 Currently pursuing B.Tech CSE at SRM Institute")
        st.info("🎯 CGPA: 9.17/10")
        st.info("🏆 Active in 4+ hackathons")
        st.info("📚 Volunteer teacher impacting 40+ students")

# SKILLS SECTION
elif selected_section == "Skills":
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)
    
    # Programming Languages
    st.markdown("### Programming Languages & Frameworks")
    skills_prog = ["Python", "Java", "HTML", "CSS", "JavaScript", "Streamlit", "MySQL", "PostgreSQL"]
    skill_html = "".join([f'<span class="skill-chip">{skill}</span>' for skill in skills_prog])
    st.markdown(skill_html, unsafe_allow_html=True)
    
    st.markdown("### Tools & Platforms")
    skills_tools = ["GitHub", "VS Code", "Canva", "Power BI", "Tableau", "MS-Excel"]
    skill_html = "".join([f'<span class="skill-chip">{skill}</span>' for skill in skills_tools])
    st.markdown(skill_html, unsafe_allow_html=True)
    
    st.markdown("### Computer Science Concepts")
    skills_cs = ["Object-Oriented Programming", "Data Structures", "Algorithms", "DBMS"]
    skill_html = "".join([f'<span class="skill-chip">{skill}</span>' for skill in skills_cs])
    st.markdown(skill_html, unsafe_allow_html=True)
    
    st.markdown("### Data Science & ML")
    skills_ml = ["Model Evaluation", "Data Cleaning", "API Integration", "Statistical Modeling", "Data Visualization", "Data Engineering"]
    skill_html = "".join([f'<span class="skill-chip">{skill}</span>' for skill in skills_ml])
    st.markdown(skill_html, unsafe_allow_html=True)

# PROJECTS SECTION
elif selected_section == "Projects":
    st.markdown('<h2 class="section-header">Featured Projects</h2>', unsafe_allow_html=True)
    
    # Project 1
    st.markdown("""
    <div class="project-card">
        <h3>🍽️ FoodBridge - Food Distribution Platform</h3>
        <p><strong>Duration:</strong> Recent Project</p>
        <p>A comprehensive food distribution platform connecting food donors with those in need, featuring real-time tracking and efficient distribution management.</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Real-time food donation tracking system</li>
            <li>Interactive dashboard for distributors</li>
            <li>User-friendly interface built with Streamlit</li>
            <li>Database integration for efficient data management</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🌐 Visit FoodBridge Live Demo", key="foodbridge"):
        st.markdown("[Click here to open FoodBridge](https://foodbridge-wpta9u8yyyjthujhwjex9i.streamlit.app/)")
    
    # Project 2
    st.markdown("""
    <div class="project-card">
        <h3>🧠 Mental Health Prediction Tool (Adolescents)</h3>
        <p><strong>Duration:</strong> Jan 2025 - Apr 2025</p>
        <p><strong>Accuracy:</strong> 92% (Random Forest) | 88% (Logistic Regression)</p>
        <p>Advanced ML model to detect stress, anxiety, and depression levels in adolescents with actionable recommendations.</p>
        <p><strong>Achievements:</strong></p>
        <ul>
            <li>92% prediction accuracy using Random Forest algorithm</li>
            <li>3x increase in user engagement through intuitive UI</li>
            <li>80% reduction in manual preprocessing steps</li>
            <li>40% improvement in usability ratings</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🌐 Visit Mental Health Tool", key="mental_health"):
        st.markdown("[Click here to open Mental Health Tool](https://adolocent-mental-health-cgqrxcpw5n5igx9ixd5ywt.streamlit.app/)")
    
    # Project 3
    st.markdown("""
    <div class="project-card">
        <h3>🤖 AI ChatBot</h3>
        <p><strong>Duration:</strong> Recent Project</p>
        <p>Intelligent chatbot application with natural language processing capabilities for interactive user experiences.</p>
        <p><strong>Features:</strong></p>
        <ul>
            <li>Natural Language Processing integration</li>
            <li>Real-time conversation capabilities</li>
            <li>User-friendly chat interface</li>
            <li>Contextual response generation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🌐 Visit ChatBot Demo", key="chatbot"):
        st.markdown("[Click here to open ChatBot](https://chatbotpy-nqfg3qsjtnjmr25d4ye5uh.streamlit.app/)")
    
    # Project 4
    st.markdown("""
    <div class="project-card">
        <h3>🗺️ Get Your Path – Smart Route Finder App</h3>
        <p><strong>Duration:</strong> Feb 2025 - Apr 2025</p>
        <p><strong>Accuracy:</strong> ~95% route accuracy</p>
        <p>Multi-page Streamlit app with real-time pathfinding using OpenRouteService API and dynamic routing logic.</p>
        <p><strong>Key Achievements:</strong></p>
        <ul>
            <li>95% route accuracy with real-time pathfinding</li>
            <li>40% reduction in search time through optimized algorithms</li>
            <li>CI/CD deployment using GitHub Actions</li>
            <li>Integration with multiple APIs for enhanced functionality</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 5
    st.markdown("""
    <div class="project-card">
        <h3>❤️ Heart Disease Prediction</h3>
        <p><strong>Duration:</strong> Jan 2024 - Feb 2024</p>
        <p><strong>Accuracy:</strong> 87% using Logistic Regression</p>
        <p>ML-powered heart disease prediction system with real-time web interface and comprehensive data visualization.</p>
        <p><strong>Technical Highlights:</strong></p>
        <ul>
            <li>87% prediction accuracy on UCI heart dataset</li>
            <li>15% performance improvement through feature engineering</li>
            <li>Sub-1-second response time with Flask integration</li>
            <li>Advanced data visualization using Matplotlib & Seaborn</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# EXPERIENCE SECTION
elif selected_section == "Experience":
    st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)
    
    # Professional Experience
    st.markdown("""
    <div class="project-card">
        <h3>🏢 Customer Service Analyst Intern</h3>
        <p><strong>Andritz Technologies Pvt Ltd</strong></p>
        <p><strong>Role:</strong> Customer Service Analyst Intern</p>
        <p>Gained valuable experience in customer service operations, data analysis, and technical support within a leading technology company.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Leadership Experience")
    
    # CodeKrafters Leadership
    st.markdown("""
    <div class="achievement-item">
        <h4>📱 Leadership at Codekrafters (formerly CodeChef)</h4>
        <ul>
            <li><strong>Campaign Success:</strong> Spearheaded HackVerse promotional campaigns, achieving 30% increase in participation</li>
            <li><strong>Content Creation:</strong> Managed social media presence with 15+ tech reels/articles monthly</li>
            <li><strong>Community Building:</strong> Built and maintained active tech community engagement</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Volunteer Experience
    st.markdown("""
    <div class="achievement-item">
        <h4>🎓 Volunteer Teacher</h4>
        <p><strong>Sri Swamy Vivekanandha Govt. Aided Elementary School, Bhavani</strong></p>
        <ul>
            <li>Taught students with zero digital access</li>
            <li>Impacted 40+ learners by introducing foundational tech literacy</li>
            <li>Developed curriculum for digital literacy programs</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # School Leadership
    st.markdown("""
    <div class="achievement-item">
        <h4>👑 School Leadership Roles</h4>
        <ul>
            <li><strong>School Pupil Leader (9th Grade):</strong> Coordinated student activities, managed 12+ school-wide events</li>
            <li><strong>Language and Literacy Minister (12th Grade):</strong> Organized 10+ literary competitions, initiated library campaign</li>
            <li><strong>Interact Club Member:</strong> Active engagement in leadership development and community service</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Hackathon Participation")
    hackathons = ["Dimohacks", "SIH Internal Hackathon", "Unfold 24", "Web3 Hackathons"]
    st.write("**Participated in:** " + " • ".join(hackathons))
    st.write("**Focus Areas:** AI/ML and Blockchain use cases")

# EDUCATION SECTION
elif selected_section == "Education":
    st.markdown('<h2 class="section-header">Education</h2>', unsafe_allow_html=True)
    
    # Current Education
    st.markdown("""
    <div class="project-card">
        <h3>🎓 Bachelor of Technology - Computer Science and Engineering</h3>
        <p><strong>SRM Institute of Science and Technology</strong></p>
        <p><strong>Duration:</strong> 2022 - 2026 (Expected)</p>
        <p><strong>CGPA:</strong> 9.17/10</p>
        <p>Pursuing comprehensive education in computer science with focus on machine learning, data structures, algorithms, and software engineering.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 12th Grade
    st.markdown("""
    <div class="achievement-item">
        <h4>🏫 12th Grade - CBSE</h4>
        <p><strong>Geethaanjali School (2022)</strong></p>
        <p><strong>Score:</strong> 69%</p>
        <p>Completed higher secondary education with focus on science and mathematics.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 10th Grade
    st.markdown("""
    <div class="achievement-item">
        <h4>🏫 10th Grade - CBSE</h4>
        <p><strong>Geethaanjali School (2020)</strong></p>
        <p><strong>Score:</strong> 75.4%</p>
        <p>Completed secondary education with strong foundation in mathematics and sciences.</p>
    </div>
    """, unsafe_allow_html=True)

# CERTIFICATIONS SECTION
elif selected_section == "Certifications":
    st.markdown('<h2 class="section-header">Certifications & Achievements</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>✈️ British Airways - Data Science Job Simulation</h3>
        <p>Completed comprehensive data science simulation focusing on real-world airline industry challenges and data analysis techniques.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>📊 Tata Group - Data Visualisation Job Simulation</h3>
        <p><strong>Focus:</strong> Empowering Business with Effective Insights</p>
        <p>Gained expertise in creating impactful data visualizations and business intelligence solutions for enterprise-level decision making.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Additional Achievements")
    achievements = [
        "🏆 30% increase in hackathon participation through promotional campaigns",
        "📈 3x user engagement improvement in mental health prediction tool",
        "⚡ 40% reduction in search time optimization for route finder app",
        "🎯 87% accuracy achieved in heart disease prediction model",
        "👥 Impacted 40+ students through digital literacy volunteering"
    ]
    
    for achievement in achievements:
        st.markdown(f"- {achievement}")

# CONTACT SECTION
elif selected_section == "Contact":
    st.markdown('<h2 class="section-header">Get In Touch</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h3>📧 Contact Information</h3>
            <p><strong>Email:</strong> st4908@srmist.edu.in</p>
            <p><strong>Phone:</strong> +91 8190002585</p>
            <p><strong>LinkedIn:</strong> linkedin.com/in/swetha-thirunavu</p>
            <p><strong>Location:</strong> Tamil Nadu, India</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 💬 Let's Connect!")
        st.write("""
        I'm always excited to discuss new opportunities, collaborate on interesting projects, 
        or just chat about technology and innovation. Feel free to reach out!
        """)
        
        st.markdown("### 🔗 Quick Links")
        if st.button("📧 Send Email"):
            st.markdown("[Click to send email](mailto:st4908@srmist.edu.in)")
        
        if st.button("💼 LinkedIn Profile"):
            st.markdown("[Visit LinkedIn Profile](https://www.linkedin.com/in/swetha-thirunavu/)")
        
        st.markdown(create_download_link(), unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>© 2025 Swetha T. Built with ❤️ using Streamlit</p>
        <p>🚀 Passionate about Machine Learning • Full-Stack Development • Community Leadership</p>
    </div>
    """, 
    unsafe_allow_html=True
)
