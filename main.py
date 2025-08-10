import streamlit as st
import base64
from PIL import Image
import requests
from io import BytesIO

# Configure the page
st.set_page_config(
    page_title="Swetha T - Portfolio",
    page_icon="💻",
    layout="wide"
)

# Custom CSS for modern tech styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 0;
        margin: 2rem auto;
        max-width: 1200px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
    }
    
    .hero-section {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: white;
        padding: 4rem 2rem;
        border-radius: 20px 20px 0 0;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse"><path d="M 50 0 L 0 0 0 50" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1"/></pattern></defs><rect width="1000" height="1000" fill="url(%23grid)"/></svg>');
        opacity: 0.3;
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
    }
    
    .main-title {
        font-size: 4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #00d4ff, #00b4d8, #0077b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
    }
    
    .subtitle {
        font-size: 1.5rem;
        font-weight: 300;
        margin-bottom: 2rem;
        color: #e0e6ed;
    }
    
    .profile-img {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        border: 4px solid #00d4ff;
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
        margin: 2rem auto;
        display: block;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .stat-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #00d4ff;
        display: block;
    }
    
    .stat-label {
        font-size: 1rem;
        color: #e0e6ed;
        margin-top: 0.5rem;
    }
    
    .content-section {
        padding: 3rem 2rem;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 600;
        color: #1a1a2e;
        margin-bottom: 2rem;
        position: relative;
        padding-left: 20px;
    }
    
    .section-title::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(45deg, #00d4ff, #0077b6);
        border-radius: 2px;
    }
    
    .about-grid {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 3rem;
        margin-bottom: 3rem;
    }
    
    .about-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #4a4a4a;
    }
    
    .info-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 15px;
        padding: 2rem;
        border-left: 4px solid #00d4ff;
    }
    
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .skill-category {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        border-top: 4px solid #00d4ff;
    }
    
    .skill-category h4 {
        color: #1a1a2e;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .skill-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    
    .skill-tag {
        background: linear-gradient(45deg, #00d4ff, #0077b6);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 500;
        transition: transform 0.3s ease;
    }
    
    .skill-tag:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 212, 255, 0.3);
    }
    
    .project-grid {
        display: grid;
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .project-card {
        background: white;
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
        border-left: 6px solid #00d4ff;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100px;
        background: linear-gradient(45deg, #00d4ff, transparent);
        opacity: 0.1;
        transform: rotate(45deg) translate(50px, -50px);
    }
    
    .project-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
    }
    
    .project-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: #1a1a2e;
        margin-bottom: 1rem;
    }
    
    .project-meta {
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 1rem;
    }
    
    .project-description {
        font-size: 1rem;
        line-height: 1.6;
        color: #555;
        margin-bottom: 1.5rem;
    }
    
    .project-highlights {
        list-style: none;
        padding: 0;
    }
    
    .project-highlights li {
        padding: 0.5rem 0;
        position: relative;
        padding-left: 1.5rem;
        color: #444;
    }
    
    .project-highlights li::before {
        content: '▶';
        position: absolute;
        left: 0;
        color: #00d4ff;
        font-size: 0.8rem;
    }
    
    .project-link {
        display: inline-block;
        background: linear-gradient(45deg, #00d4ff, #0077b6);
        color: white;
        padding: 1rem 2rem;
        border-radius: 30px;
        text-decoration: none;
        font-weight: 600;
        margin-top: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0, 212, 255, 0.3);
    }
    
    .project-link:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 212, 255, 0.4);
    }
    
    .experience-grid {
        display: grid;
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .experience-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #28a745;
    }
    
    .experience-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1a1a2e;
        margin-bottom: 0.5rem;
    }
    
    .experience-company {
        font-weight: 500;
        color: #00d4ff;
        margin-bottom: 1rem;
    }
    
    .contact-section {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: white;
        padding: 4rem 2rem;
        border-radius: 0 0 20px 20px;
        text-align: center;
    }
    
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .contact-item {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .contact-links {
        margin-top: 2rem;
    }
    
    .contact-btn {
        display: inline-block;
        background: linear-gradient(45deg, #00d4ff, #0077b6);
        color: white;
        padding: 1rem 2rem;
        border-radius: 30px;
        text-decoration: none;
        font-weight: 600;
        margin: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .contact-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 212, 255, 0.4);
    }
    
    .download-cv {
        background: linear-gradient(45deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 1.2rem 2.5rem;
        border: none;
        border-radius: 30px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        margin: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(255, 107, 107, 0.3);
    }
    
    .download-cv:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(255, 107, 107, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <h1 class="main-title">SWETHA T</h1>
        <p class="subtitle">Machine Learning Engineer • Full-Stack Developer • Tech Innovator</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Profile image and stats
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    try:
        # Display the uploaded profile photo
        st.image("https://i.ibb.co/YhFX4kL/swetha-profile.jpg", 
                 width=200, 
                 use_column_width=False)
    except:
        st.image("https://via.placeholder.com/200x200/00d4ff/ffffff?text=S", width=200)

# Stats in hero section
st.markdown("""
<div style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); padding: 2rem; margin-top: -1rem;">
    <div class="stats-grid">
        <div class="stat-card">
            <span class="stat-number">9.17</span>
            <div class="stat-label">CGPA</div>
        </div>
        <div class="stat-card">
            <span class="stat-number">3</span>
            <div class="stat-label">Live Projects</div>
        </div>
        <div class="stat-card">
            <span class="stat-number">92%</span>
            <div class="stat-label">ML Accuracy</div>
        </div>
        <div class="stat-card">
            <span class="stat-number">40+</span>
            <div class="stat-label">Students Mentored</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# About Section
st.markdown("""
<div class="content-section">
    <h2 class="section-title">About Me</h2>
    <div class="about-grid">
        <div class="about-text">
            <p>Passionate <strong>Computer Science Engineering student</strong> specializing in Machine Learning and Full-Stack Development. I build intelligent systems that solve real-world problems, from mental health prediction tools achieving 92% accuracy to smart route-finding applications serving thousands of users.</p>
            
            <p>My expertise spans the entire development lifecycle - from data preprocessing and model training to deployment and user experience optimization. I've led technical communities, mentored students in digital literacy, and consistently delivered impactful solutions that drive measurable results.</p>
            
            <p><strong>What drives me:</strong> The intersection of cutting-edge technology and social impact. Every project I build aims to make technology more accessible and beneficial for everyone.</p>
        </div>
        <div class="info-card">
            <h4>🎓 Education</h4>
            <p><strong>B.Tech Computer Science</strong><br>
            SRM Institute of Science Technology<br>
            <strong>CGPA:</strong> 9.17 | <strong>Expected:</strong> 2026</p>
            
            <br>
            
            <a href="#" class="download-cv" onclick="alert('CV download will be implemented with your PDF file')">📄 Download Resume</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Skills Section
st.markdown("""
<div class="content-section">
    <h2 class="section-title">Technical Expertise</h2>
    <div class="skills-grid">
        <div class="skill-category">
            <h4>🚀 Programming & Frameworks</h4>
            <div class="skill-tags">
                <span class="skill-tag">Python</span>
                <span class="skill-tag">Java</span>
                <span class="skill-tag">JavaScript</span>
                <span class="skill-tag">HTML5</span>
                <span class="skill-tag">CSS3</span>
                <span class="skill-tag">Streamlit</span>
                <span class="skill-tag">Flask</span>
            </div>
        </div>
        <div class="skill-category">
            <h4>🤖 Machine Learning & Data</h4>
            <div class="skill-tags">
                <span class="skill-tag">Random Forest</span>
                <span class="skill-tag">Logistic Regression</span>
                <span class="skill-tag">Data Preprocessing</span>
                <span class="skill-tag">Model Evaluation</span>
                <span class="skill-tag">Statistical Analysis</span>
                <span class="skill-tag">Data Visualization</span>
            </div>
        </div>
        <div class="skill-category">
            <h4>🛠️ Tools & Platforms</h4>
            <div class="skill-tags">
                <span class="skill-tag">GitHub</span>
                <span class="skill-tag">VS Code</span>
                <span class="skill-tag">MySQL</span>
                <span class="skill-tag">PostgreSQL</span>
                <span class="skill-tag">Power BI</span>
                <span class="skill-tag">Tableau</span>
                <span class="skill-tag">GitHub Actions</span>
            </div>
        </div>
        <div class="skill-category">
            <h4>💡 Core Concepts</h4>
            <div class="skill-tags">
                <span class="skill-tag">Data Structures</span>
                <span class="skill-tag">Algorithms</span>
                <span class="skill-tag">OOP</span>
                <span class="skill-tag">DBMS</span>
                <span class="skill-tag">API Development</span>
                <span class="skill-tag">CI/CD</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Projects Section
st.markdown("""
<div class="content-section">
    <h2 class="section-title">Featured Projects</h2>
    <div class="project-grid">
""", unsafe_allow_html=True)

# Project 1 - Mental Health Tool
st.markdown("""
        <div class="project-card">
            <h3 class="project-title">🧠 Mental Health Prediction Tool</h3>
            <div class="project-meta">Jan 2025 - Apr 2025 • Machine Learning • Streamlit</div>
            <div class="project-description">
                Advanced ML system detecting stress, anxiety, and depression in adolescents with 92% accuracy. 
                Features automated preprocessing, intuitive multi-tab UI, and personalized wellness recommendations.
            </div>
            <ul class="project-highlights">
                <li><strong>92% prediction accuracy</strong> using Random Forest algorithm</li>
                <li><strong>3x increase in user engagement</strong> through optimized UX design</li>
                <li><strong>80% reduction in preprocessing time</strong> with automated pipelines</li>
                <li><strong>Real-time predictions</strong> with actionable mental health insights</li>
            </ul>
            <a href="https://adolocent-mental-health-cgqrxcpw5n5igx9ixd5ywt.streamlit.app/" target="_blank" class="project-link">🚀 View Live Demo</a>
        </div>
""", unsafe_allow_html=True)

# Project 2 - FoodBridge
st.markdown("""
        <div class="project-card">
            <h3 class="project-title">🍽️ FoodBridge - Smart Distribution Platform</h3>
            <div class="project-meta">2024 • Full-Stack Development • Database Design</div>
            <div class="project-description">
                Comprehensive food distribution platform connecting donors with recipients. Features real-time tracking, 
                intelligent matching algorithms, and responsive dashboard for efficient resource management.
            </div>
            <ul class="project-highlights">
                <li><strong>Real-time tracking system</strong> for donation lifecycle</li>
                <li><strong>Intelligent matching</strong> between donors and recipients</li>
                <li><strong>Multi-role dashboard</strong> for admins, donors, and distributors</li>
                <li><strong>Mobile-responsive design</strong> for accessibility</li>
            </ul>
            <a href="https://foodbridge-wpta9u8yyyjthujhwjex9i.streamlit.app/" target="_blank" class="project-link">🚀 View Live Demo</a>
        </div>
""", unsafe_allow_html=True)

# Project 3 - Get Your Path
st.markdown("""
        <div class="project-card">
            <h3 class="project-title">🗺️ Get Your Path - Smart Navigation</h3>
            <div class="project-meta">Feb 2025 - Apr 2025 • API Integration • Route Optimization</div>
            <div class="project-description">
                Intelligent route-finding application with 95% accuracy using OpenRouteService API. 
                Features dynamic routing algorithms, real-time optimization, and seamless user experience.
            </div>
            <ul class="project-highlights">
                <li><strong>95% route accuracy</strong> with real-time pathfinding</li>
                <li><strong>40% faster search times</strong> through algorithm optimization</li>
                <li><strong>Multiple routing options</strong> (shortest, fastest, recommended)</li>
                <li><strong>CI/CD deployment</strong> with automated testing</li>
            </ul>
            <div style="margin-top: 1rem; padding: 1rem; background: rgba(255, 193, 7, 0.1); border-radius: 10px; border-left: 4px solid #ffc107;">
                <strong>🚧 Coming Soon:</strong> Final deployment in progress
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Experience Section
st.markdown("""
<div class="content-section">
    <h2 class="section-title">Professional Experience</h2>
    <div class="experience-grid">
        <div class="experience-card">
            <h3 class="experience-title">💼 Customer Service Analyst Intern</h3>
            <div class="experience-company">Andritz Technologies Pvt Ltd</div>
            <p>Gained comprehensive experience in enterprise-level customer service operations, technical support systems, 
            and data analysis workflows. Contributed to process improvements and customer satisfaction initiatives.</p>
        </div>
        
        <div class="experience-card">
            <h3 class="experience-title">📱 Technical Community Leader</h3>
            <div class="experience-company">Codekrafters (formerly CodeChef)</div>
            <ul class="project-highlights">
                <li><strong>30% increase</strong> in HackVerse participation through strategic campaigns</li>
                <li>Managed social media presence with <strong>15+ monthly tech content</strong></li>
                <li>Built and maintained active developer community engagement</li>
            </ul>
        </div>
        
        <div class="experience-card">
            <h3 class="experience-title">🎓 Digital Literacy Volunteer</h3>
            <div class="experience-company">Sri Swamy Vivekanandha Govt. School</div>
            <ul class="project-highlights">
                <li>Taught foundational tech skills to <strong>40+ students</strong></li>
                <li>Developed curriculum for students with zero digital access</li>
                <li>Created sustainable learning programs for continued impact</li>
            </ul>
        </div>
        
        <div class="experience-card">
            <h3 class="experience-title">🏆 Active Hackathon Participant</h3>
            <div class="experience-company">Multiple Platforms</div>
            <p><strong>Participated in:</strong> Dimohacks, SIH Internal Hackathon, Unfold 24, Web3 Hackathons<br>
            <strong>Focus Areas:</strong> AI/ML solutions and blockchain applications</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="contact-section">
    <h2 style="font-size: 2.5rem; margin-bottom: 1rem;">Let's Build Something Amazing Together</h2>
    <p style="font-size: 1.2rem; margin-bottom: 2rem;">Open to collaborations, opportunities, and innovative projects</p>
    
    <div class="contact-grid">
        <div class="contact-item">
            <h4>📧 Email</h4>
            <p>st4908@srmist.edu.in</p>
        </div>
        <div class="contact-item">
            <h4>📱 Phone</h4>
            <p>+91 8190002585</p>
        </div>
        <div class="contact-item">
            <h4>💼 LinkedIn</h4>
            <p>swetha-thirunavu</p>
        </div>
        <div class="contact-item">
            <h4>📍 Location</h4>
            <p>Tamil Nadu, India</p>
        </div>
    </div>
    
    <div class="contact-links">
        <a href="mailto:st4908@srmist.edu.in" class="contact-btn">📧 Send Email</a>
        <a href="https://www.linkedin.com/in/swetha-thirunavu/" target="_blank" class="contact-btn">💼 LinkedIn Profile</a>
        <a href="#" class="contact-btn" onclick="alert('GitHub profile link can be added here')">💻 GitHub</a>
    </div>
    
    <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.2);">
        <p style="font-size: 1rem; opacity: 0.8;">© 2025 Swetha T • Built with passion for technology and innovation</p>
        <p style="font-size: 0.9rem; opacity: 0.6; margin-top: 0.5rem;">Machine Learning • Full-Stack Development • Community Impact</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
