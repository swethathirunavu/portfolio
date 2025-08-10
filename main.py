import streamlit as st
import base64
from PIL import Image
import requests
from io import BytesIO

# Configure the page
st.set_page_config(
    page_title="Swetha T - Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.3rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2.2rem;
        font-weight: bold;
        color: #1f77b4;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
    }
    .project-card {
        background: linear-gradient(145deg, #f0f2f6, #ffffff);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
        border-left: 5px solid #1f77b4;
        transition: transform 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }
    .skill-chip {
        background: linear-gradient(45deg, #1f77b4, #0d5aa7);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        margin: 0.3rem;
        display: inline-block;
        font-weight: 500;
    }
    .contact-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-top: 2rem;
    }
    .achievement-item {
        background: linear-gradient(145deg, #f8f9fa, #e9ecef);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #28a745;
    }
    .download-cv {
        background: linear-gradient(45deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 1.2rem 2.5rem;
        border: none;
        border-radius: 30px;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        margin: 1.5rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
    }
    .download-cv:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
    }
    .project-link-btn {
        background: linear-gradient(45deg, #28a745, #20c997);
        color: white;
        padding: 0.8rem 1.5rem;
        border: none;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    .project-link-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(40, 167, 69, 0.3);
    }
    .stats-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 2rem 0;
    }
    .profile-container {
        text-align: center;
        margin-bottom: 3rem;
    }
    .profile-img {
        border-radius: 50%;
        border: 5px solid #1f77b4;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Function to create download link for CV
def create_download_link():
    return """
    <a href="#" class="download-cv" onclick="alert('CV download feature will be implemented with actual PDF file')">
        📄 Download CV
    </a>
    """

# HEADER SECTION
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="profile-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-header">SWETHA T</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Computer Science Engineering Student | Machine Learning Enthusiast | Full-Stack Developer</p>', unsafe_allow_html=True)
    
    # Display the uploaded profile photo
    try:
        # This will display the uploaded image in real-time
        st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCACAAIADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD//2Q==", 
                 width=250, 
                 use_column_width=False)
    except:
        # Fallback to placeholder if image fails to load
        st.image("https://via.placeholder.com/250x250/1f77b4/ffffff?text=SWETHA+T", width=250)
    
    st.markdown(create_download_link(), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# QUICK STATS
st.markdown("""
<div class="stats-container">
    <h3 style="margin-bottom: 1.5rem;">📊 Quick Stats</h3>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
        <div style="margin: 0.5rem;">
            <h2 style="margin: 0;">9.17</h2>
            <p style="margin: 0;">CGPA</p>
        </div>
        <div style="margin: 0.5rem;">
            <h2 style="margin: 0;">3</h2>
            <p style="margin: 0;">Live Projects</p>
        </div>
        <div style="margin: 0.5rem;">
            <h2 style="margin: 0;">92%</h2>
            <p style="margin: 0;">Best ML Accuracy</p>
        </div>
        <div style="margin: 0.5rem;">
            <h2 style="margin: 0;">40+</h2>
            <p style="margin: 0;">Students Impacted</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ABOUT SECTION
st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    **Passionate and self-driven B.Tech Computer Science student** with strong skills in Machine Learning (ML), 
    JavaScript, HTML, CSS, Streamlit, and Python. Proficient in applying Data Structures and Algorithms (DSA) 
    to build efficient, real-world solutions.
    
    Known for developing impactful projects like smart route-finding apps and adolescent mental health prediction tools. 
    Currently working as a **Customer Service Analyst Intern at Andritz Technologies Pvt Ltd**, gaining valuable 
    experience in enterprise-level operations and technical support.
    
    **Leadership Experience**: Spearheaded HackVerse promotional campaigns at Codekrafters (formerly CodeChef), 
    leading to a 30% increase in participation. Passionate about social impact, having volunteered to teach 
    digital literacy to 40+ students with zero digital access.
    """)

with col2:
    st.markdown("### 🎓 Current Education")
    st.info("**B.Tech CSE** - SRM Institute of Science Technology\n**CGPA:** 9.17 (Expected: 2026)")
    
    st.markdown("### 💼 Current Role")
    st.success("**Customer Service Analyst Intern**\nAndritz Technologies Pvt Ltd")

# SKILLS SECTION
st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Programming & Frameworks")
    skills_prog = ["Python", "Java", "HTML", "CSS", "JavaScript", "Streamlit", "MySQL", "PostgreSQL"]
    skill_html = "".join([f'<span class="skill-chip">{skill}</span>' for skill in skills_prog])
    st.markdown(skill_html, unsafe_allow_html=True)
    
    st.markdown("### Data Science & ML")
    skills_ml = ["Model Evaluation", "Data Cleaning", "API Integration", "Statistical Modeling", "Data Visualization", "Random Forest", "Logistic Regression"]
    skill_html = "".join([f'<span class="skill-chip">{skill}</span>' for skill in skills_ml])
    st.markdown(skill_html, unsafe_allow_html=True)

with col2:
    st.markdown("### Tools & Platforms")
    skills_tools = ["GitHub", "VS Code", "Power BI", "Tableau", "MS-Excel", "Flask", "GitHub Actions"]
    skill_html = "".join([f'<span class="skill-chip">{skill}</span>' for skill in skills_tools])
    st.markdown(skill_html, unsafe_allow_html=True)
    
    st.markdown("### Core CS Concepts")
    skills_cs = ["OOP", "Data Structures", "Algorithms", "DBMS", "CI/CD", "API Development"]
    skill_html = "".join([f'<span class="skill-chip">{skill}</span>' for skill in skills_cs])
    st.markdown(skill_html, unsafe_allow_html=True)

# PROJECTS SECTION
st.markdown('<h2 class="section-header">Featured Projects</h2>', unsafe_allow_html=True)

# Project 1 - FoodBridge
st.markdown("""
<div class="project-card">
    <h3>🍽️ FoodBridge - Food Distribution Platform</h3>
    <p><strong>Tech Stack:</strong> Streamlit, Python, Database Integration, Real-time Tracking</p>
    <p>A comprehensive food distribution platform connecting food donors with those in need, featuring an intuitive 
    dashboard for efficient distribution management and real-time tracking capabilities.</p>
    <p><strong>Key Features:</strong></p>
    <ul>
        <li>🔄 Real-time food donation tracking system</li>
        <li>📊 Interactive dashboard for distributors and administrators</li>
        <li>🎯 User-friendly interface with multi-tab navigation</li>
        <li>💾 Robust database integration for efficient data management</li>
        <li>📱 Responsive design for mobile and desktop access</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin: 1rem 0;">
    <a href="https://foodbridge-wpta9u8yyyjthujhwjex9i.streamlit.app/" 
       target="_blank" class="project-link-btn">🌐 View Live Demo</a>
</div>
""", unsafe_allow_html=True)

# Project 2 - Mental Health Tool
st.markdown("""
<div class="project-card">
    <h3>🧠 Mental Health Prediction Tool (Adolescents)</h3>
    <p><strong>Duration:</strong> Jan 2025 - Apr 2025 | <strong>Accuracy:</strong> 92% (Random Forest) | 88% (Logistic Regression)</p>
    <p><strong>Tech Stack:</strong> Python, Streamlit, Random Forest, Logistic Regression, LabelEncoder, StandardScaler</p>
    <p>Advanced machine learning model designed to detect stress, anxiety, and depression levels in adolescents, 
    providing actionable mental wellness recommendations based on prediction outcomes.</p>
    <p><strong>Key Achievements:</strong></p>
    <ul>
        <li>🎯 <strong>92% prediction accuracy</strong> using Random Forest algorithm</li>
        <li>📈 <strong>3x increase in user engagement</strong> through intuitive multi-tab UI</li>
        <li>⚡ <strong>80% reduction in manual preprocessing</strong> steps with automated data handling</li>
        <li>✅ <strong>40% improvement in usability ratings</strong> from user feedback</li>
        <li>💡 Provides personalized mental wellness tips and suggestions</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin: 1rem 0;">
    <a href="https://adolocent-mental-health-cgqrxcpw5n5igx9ixd5ywt.streamlit.app/" 
       target="_blank" class="project-link-btn">🌐 View Live Demo</a>
</div>
""", unsafe_allow_html=True)

# Project 3 - Get Your Path
st.markdown("""
<div class="project-card">
    <h3>🗺️ Get Your Path – Smart Route Finder App</h3>
    <p><strong>Duration:</strong> Feb 2025 - Apr 2025 | <strong>Accuracy:</strong> ~95% route accuracy</p>
    <p><strong>Tech Stack:</strong> Streamlit, OpenRouteService API, GitHub Actions, Mapbox Integration, Python</p>
    <p>Sophisticated multi-page route-finding application with real-time pathfinding capabilities, dynamic routing 
    algorithms, and seamless API integrations for optimal navigation experience.</p>
    <p><strong>Technical Highlights:</strong></p>
    <ul>
        <li>🎯 <strong>~95% route accuracy</strong> with real-time pathfinding using OpenRouteService API</li>
        <li>⚡ <strong>40% reduction in search time</strong> through optimized routing algorithms</li>
        <li>🔄 Dynamic alternate routing logic (shortest, fastest, recommended paths)</li>
        <li>🚀 CI/CD deployment using <strong>GitHub Actions</strong> on Streamlit Cloud</li>
        <li>🗺️ Planned integration with Mapbox autocomplete and Geolocation API</li>
        <li>🤖 Future LLM chatbot integration for interactive navigation</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin: 1rem 0;">
    <p><em>🚧 Live demo coming soon - Currently in final deployment phase</em></p>
</div>
""", unsafe_allow_html=True)

# EXPERIENCE & LEADERSHIP SECTION
st.markdown('<h2 class="section-header">Experience & Leadership</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="achievement-item">
        <h4>🏢 Customer Service Analyst Intern</h4>
        <p><strong>Andritz Technologies Pvt Ltd</strong></p>
        <p>Gained valuable experience in enterprise operations, customer service management, 
        data analysis, and technical support in a leading technology company environment.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="achievement-item">
        <h4>🎓 Volunteer Teacher</h4>
        <p><strong>Sri Swamy Vivekanandha Govt. School</strong></p>
        <ul>
            <li>Taught digital literacy to 40+ students</li>
            <li>Introduced foundational tech concepts</li>
            <li>Impacted students with zero digital access</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="achievement-item">
        <h4>📱 Leadership at Codekrafters</h4>
        <p><strong>(formerly CodeChef Chapter)</strong></p>
        <ul>
            <li><strong>30% increase</strong> in HackVerse participation</li>
            <li>Managed social media with 15+ monthly posts</li>
            <li>Built active tech community engagement</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="achievement-item">
        <h4>🏆 Hackathon Participation</h4>
        <ul>
            <li>Dimohacks, SIH Internal Hackathon</li>
            <li>Unfold 24, Web3 Hackathons</li>
            <li>Focus: AI/ML and Blockchain solutions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# CERTIFICATIONS
st.markdown('<h2 class="section-header">Certifications</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="project-card">
        <h4>✈️ British Airways - Data Science Job Simulation</h4>
        <p>Comprehensive data science simulation focusing on airline industry challenges and advanced analytics.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-card">
        <h4>📊 Tata Group - Data Visualisation Job Simulation</h4>
        <p>Specialized in creating business intelligence solutions and impactful data visualizations.</p>
    </div>
    """, unsafe_allow_html=True)

# CONTACT SECTION
st.markdown('<h2 class="section-header">Let\'s Connect!</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="contact-info">
    <h3>📧 Contact Information</h3>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin-top: 1.5rem;">
        <div style="margin: 0.5rem;">
            <p><strong>📧 Email:</strong><br>st4908@srmist.edu.in</p>
        </div>
        <div style="margin: 0.5rem;">
            <p><strong>📱 Phone:</strong><br>+91 8190002585</p>
        </div>
        <div style="margin: 0.5rem;">
            <p><strong>💼 LinkedIn:</strong><br>linkedin.com/in/swetha-thirunavu</p>
        </div>
        <div style="margin: 0.5rem;">
            <p><strong>📍 Location:</strong><br>Tamil Nadu, India</p>
        </div>
    </div>
    <div style="margin-top: 2rem;">
        <a href="mailto:st4908@srmist.edu.in" class="project-link-btn">📧 Send Email</a>
        <a href="https://www.linkedin.com/in/swetha-thirunavu/" target="_blank" class="project-link-btn">💼 LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p style="font-size: 1.1rem; margin-bottom: 1rem;">
            🚀 <strong>Open to Opportunities:</strong> Internships • Full-time Roles • Collaborative Projects
        </p>
        <p>© 2025 Swetha T. Built with ❤️ using Streamlit</p>
        <p style="font-style: italic;">Passionate about Machine Learning • Full-Stack Development • Community Impact</p>
    </div>
    """, 
    unsafe_allow_html=True
)
