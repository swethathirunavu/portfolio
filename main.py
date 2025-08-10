import streamlit as st
from PIL import Image
import base64

# Configure the page
st.set_page_config(
    page_title="Swetha T - Machine Learning Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Direct conversion from your HTML
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .stApp {
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
        color: #e2e8f0;
        background: #0a0a0a;
    }
    
    .main .block-container {
        padding-top: 0;
        padding-bottom: 0;
        max-width: none;
    }

    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stAppHeader {display: none;}

    html {
        scroll-behavior: smooth;
    }

    /* Header */
    .header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background: rgba(10, 10, 10, 0.95);
        backdrop-filter: blur(20px);
        z-index: 1000;
        padding: 1rem 0;
        transition: all 0.3s ease;
        border-bottom: 1px solid rgba(59, 130, 246, 0.2);
    }

    .nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
    }

    .logo {
        font-size: 1.8rem;
        font-weight: 800;
        color: #3b82f6;
        text-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
    }

    .nav-links {
        display: flex;
        list-style: none;
        gap: 2rem;
    }

    .nav-links a {
        text-decoration: none;
        color: #e2e8f0;
        font-weight: 500;
        transition: all 0.3s ease;
        position: relative;
        padding: 0.5rem 1rem;
        border-radius: 8px;
    }

    .nav-links a:hover {
        background: rgba(59, 130, 246, 0.1);
        color: #3b82f6;
    }

    /* Hero Section */
    .hero {
        min-height: 100vh;
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: white;
        position: relative;
        overflow: hidden;
    }

    .hero::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse"><path d="M 50 0 L 0 0 0 50" fill="none" stroke="rgba(59,130,246,0.1)" stroke-width="1"/></pattern></defs><rect width="1000" height="1000" fill="url(%23grid)"/></svg>');
        opacity: 0.5;
    }

    .hero-content {
        z-index: 2;
        max-width: 900px;
        padding: 0 2rem;
        animation: fadeInUp 1s ease-out;
    }

    .profile-img {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        border: 3px solid rgba(59, 130, 246, 0.5);
        margin: 0 auto 2rem;
        display: block;
        box-shadow: 0 20px 60px rgba(59, 130, 246, 0.2);
        animation: float 6s ease-in-out infinite;
        object-fit: cover;
        object-position: center;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1rem;
        color: #ffffff;
    }

    .hero-subtitle {
        font-size: 1.5rem;
        font-weight: 400;
        margin-bottom: 2rem;
        color: #3b82f6;
        opacity: 0.9;
    }

    .hero-description {
        font-size: 1.1rem;
        margin-bottom: 3rem;
        color: #cbd5e0;
        opacity: 0.8;
        line-height: 1.8;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }

    .hero-buttons {
        display: flex;
        gap: 1rem;
        justify-content: center;
        flex-wrap: wrap;
        margin-bottom: 3rem;
    }

    .btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 1rem 2rem;
        background: rgba(59, 130, 246, 0.1);
        color: white;
        text-decoration: none;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        border: 2px solid rgba(59, 130, 246, 0.3);
        backdrop-filter: blur(10px);
        cursor: pointer;
    }

    .btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.2);
        background: rgba(59, 130, 246, 0.2);
        border-color: #3b82f6;
    }

    .btn-primary {
        background: #3b82f6;
        color: #ffffff;
        border-color: #3b82f6;
        font-weight: 700;
    }

    .btn-primary:hover {
        background: #2563eb;
        color: #ffffff;
        transform: translateY(-2px);
    }

    /* Stats */
    .stats {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        margin: 2rem auto 0;
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid rgba(59, 130, 246, 0.2);
        max-width: 800px;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 2rem;
        text-align: center;
    }

    .stat-item {
        animation: countUp 2s ease-out;
    }

    .stat-number {
        display: block;
        font-size: 2.5rem;
        font-weight: 800;
        color: #3b82f6;
        margin-bottom: 0.5rem;
    }

    .stat-label {
        font-size: 1rem;
        color: #cbd5e0;
        opacity: 0.8;
    }

    /* Sections */
    .section {
        padding: 5rem 0;
        max-width: 1200px;
        margin: 0 auto;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    .section-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 3rem;
        color: #ffffff;
        position: relative;
    }

    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: #3b82f6;
        border-radius: 2px;
    }

    /* About Section */
    .about {
        background: linear-gradient(135deg, #111111 0%, #1a1a2e 100%);
    }

    .about-content {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 4rem;
        align-items: start;
    }

    .about-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #cbd5e0;
    }

    .about-text h3 {
        color: #3b82f6;
        margin-bottom: 1rem;
        font-size: 1.5rem;
        font-weight: 600;
    }

    .about-text p {
        margin-bottom: 1.5rem;
    }

    .about-text strong {
        color: #60a5fa;
    }

    .about-info {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        border-left: 4px solid #3b82f6;
    }

    .info-item {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        font-size: 1rem;
        color: #cbd5e0;
    }

    .info-item i {
        color: #3b82f6;
        margin-right: 1rem;
        width: 20px;
    }

    .info-item strong {
        color: #60a5fa;
    }

    /* Skills Section */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    .skill-category {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        border-top: 4px solid #3b82f6;
        transition: transform 0.3s ease;
    }

    .skill-category:hover {
        transform: translateY(-5px);
    }

    .skill-category h3 {
        color: #3b82f6;
        margin-bottom: 1.5rem;
        font-size: 1.3rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .skill-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }

    .skill-tag {
        background: rgba(59, 130, 246, 0.2);
        color: #93c5fd;
        border: 1px solid rgba(59, 130, 246, 0.3);
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-size: 0.9rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }

    .skill-tag:hover {
        transform: translateY(-2px);
        background: rgba(59, 130, 246, 0.3);
        border-color: #3b82f6;
    }

    /* Projects Section */
    .projects-grid {
        display: grid;
        gap: 3rem;
        margin-top: 3rem;
    }

    .project-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
        border-left: 6px solid #3b82f6;
    }

    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4);
    }

    .project-content {
        padding: 2.5rem;
    }

    .project-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 1rem;
    }

    .project-meta {
        font-size: 0.9rem;
        color: #94a3b8;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        flex-wrap: wrap;
    }

    .project-meta i {
        color: #3b82f6;
    }

    .project-description {
        font-size: 1rem;
        line-height: 1.6;
        color: #cbd5e0;
        margin-bottom: 1.5rem;
    }

    .project-highlights {
        list-style: none;
        margin-bottom: 2rem;
    }

    .project-highlights li {
        padding: 0.5rem 0;
        position: relative;
        padding-left: 1.5rem;
        color: #cbd5e0;
    }

    .project-highlights li::before {
        content: '✓';
        position: absolute;
        left: 0;
        color: #10b981;
        font-weight: bold;
    }

    .project-highlights strong {
        color: #3b82f6;
    }

    .project-link {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: #3b82f6;
        color: #ffffff;
        padding: 1rem 2rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .project-link:hover {
        transform: translateY(-2px);
        background: #2563eb;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.2);
    }

    /* Experience Section */
    .experience {
        background: linear-gradient(135deg, #111111 0%, #1a1a2e 100%);
    }

    .experience-grid {
        display: grid;
        gap: 2rem;
        margin-top: 3rem;
    }

    .experience-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 2.5rem;
        border-radius: 12px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        border-left: 4px solid #10b981;
        transition: transform 0.3s ease;
    }

    .experience-card:hover {
        transform: translateY(-3px);
    }

    .experience-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }

    .experience-company {
        font-size: 1.1rem;
        color: #3b82f6;
        margin-bottom: 1rem;
        font-weight: 500;
    }

    .experience-description {
        color: #cbd5e0;
        line-height: 1.6;
    }

    /* Contact Section */
    .contact {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
        color: white;
        text-align: center;
    }

    .contact .section-title {
        color: #ffffff;
    }

    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }

    .contact-item {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 2rem;
        border: 1px solid rgba(59, 130, 246, 0.2);
        transition: all 0.3s ease;
    }

    .contact-item:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: translateY(-3px);
    }

    .contact-item i {
        font-size: 2rem;
        color: #3b82f6;
        margin-bottom: 1rem;
    }

    .contact-item h3 {
        margin-bottom: 0.5rem;
        font-size: 1.2rem;
        color: #ffffff;
    }

    .contact-links {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 3rem;
        flex-wrap: wrap;
    }

    .contact-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: #3b82f6;
        color: #ffffff;
        padding: 1rem 2rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        cursor: pointer;
        border: none;
    }

    .contact-btn:hover {
        background: #2563eb;
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.2);
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        background: #0a0a0a;
        color: #9ca3af;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }

        .hero-subtitle {
            font-size: 1.2rem;
        }

        .section-title {
            font-size: 2rem;
        }

        .about-content {
            grid-template-columns: 1fr;
            gap: 2rem;
        }

        .skills-grid {
            grid-template-columns: 1fr;
        }

        .hero-buttons {
            flex-direction: column;
            align-items: center;
        }

        .btn {
            width: 100%;
            max-width: 300px;
            justify-content: center;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header Navigation
st.markdown("""
<header class="header">
    <nav class="nav">
        <div class="logo">Swetha T</div>
        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#experience">Experience</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
</header>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<section id="home" class="hero">
    <div class="hero-content">
        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==" alt="Swetha T" class="profile-img">
        
        <h1 class="hero-title">Swetha T</h1>
        <p class="hero-subtitle">Machine Learning Engineer • Data Analysis Specialist • Tech Innovator</p>
        <p class="hero-description">
            Passionate Computer Science student building intelligent systems that solve real-world problems. 
            Specializing in ML models with 92% accuracy, advanced data analysis, and impactful tech solutions.
        </p>
        <div class="hero-buttons">
            <a href="#projects" class="btn btn-primary">
                <i class="fas fa-rocket"></i>
                View My Work
            </a>
            <a href="#contact" class="btn">
                <i class="fas fa-envelope"></i>
                Get In Touch
            </a>
            <a href="https://drive.google.com/file/d/1T24Cz7J6VVmRWKh3DToTuR6LvfNMeYGA/view?usp=sharing" target="_blank" class="btn">
                <i class="fas fa-download"></i>
                Download CV
            </a>
        </div>
        
        <div class="stats">
            <div class="stats-grid">
                <div class="stat-item">
                    <span class="stat-number">9.17</span>
                    <div class="stat-label">CGPA</div>
                </div>
                <div class="stat-item">
                    <span class="stat-number">3</span>
                    <div class="stat-label">Live Projects</div>
                </div>
                <div class="stat-item">
                    <span class="stat-number">92%</span>
                    <div class="stat-label">ML Accuracy</div>
                </div>
                <div class="stat-item">
                    <span class="stat-number">40+</span>
                    <div class="stat-label">Students Mentored</div>
                </div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# About Section
st.markdown("""
<section id="about" class="about">
    <div class="section">
        <h2 class="section-title">About Me</h2>
        <div class="about-content">
            <div class="about-text">
                <h3>Passionate about Innovation</h3>
                <p>
                    I'm a <strong>Computer Science student</strong> with a deep passion for creating intelligent systems 
                    that make a real difference. My journey in tech has been driven by curiosity and the desire to 
                    solve complex problems through innovative solutions.
                </p>
                
                <h3>Technical Excellence</h3>
                <p>
                    With expertise in <strong>Machine Learning, Data Analysis, and Software Development</strong>, 
                    I've built ML models achieving <strong>92% accuracy</strong> and developed applications that 
                    serve real users. My work spans from predictive analytics to full-stack web development.
                </p>
                
                <h3>Leadership & Mentorship</h3>
                <p>
                    Beyond technical skills, I'm committed to knowledge sharing and community building. 
                    I've mentored <strong>40+ students</strong> in programming and development, helping them 
                    navigate their tech journey and build successful careers.
                </p>
            </div>
            
            <div class="about-info">
                <div class="info-item">
                    <i class="fas fa-graduation-cap"></i>
                    <strong>Education:</strong> Computer Science Engineering
                </div>
                <div class="info-item">
                    <i class="fas fa-star"></i>
                    <strong>CGPA:</strong> 9.17/10
                </div>
                <div class="info-item">
                    <i class="fas fa-map-marker-alt"></i>
                    <strong>Location:</strong> Tamil Nadu, India
                </div>
                <div class="info-item">
                    <i class="fas fa-envelope"></i>
                    <strong>Email:</strong> swethamurugesan2110@gmail.com
                </div>
                <div class="info-item">
                    <i class="fas fa-phone"></i>
                    <strong>Phone:</strong> +91 7358749978
                </div>
                <div class="info-item">
                    <i class="fab fa-linkedin"></i>
                    <strong>LinkedIn:</strong> linkedin.com/in/swetha-t-0a3a64252
                </div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Skills Section
st.markdown("""
<section id="skills" class="section">
    <h2 class="section-title">Skills & Technologies</h2>
    <div class="skills-grid">
        <div class="skill-category">
            <h3><i class="fas fa-brain"></i> Machine Learning & AI</h3>
            <div class="skill-tags">
                <span class="skill-tag">Python</span>
                <span class="skill-tag">Scikit-learn</span>
                <span class="skill-tag">TensorFlow</span>
                <span class="skill-tag">Pandas</span>
                <span class="skill-tag">NumPy</span>
                <span class="skill-tag">Matplotlib</span>
                <span class="skill-tag">Seaborn</span>
                <span class="skill-tag">Jupyter</span>
            </div>
        </div>
        
        <div class="skill-category">
            <h3><i class="fas fa-code"></i> Programming Languages</h3>
            <div class="skill-tags">
                <span class="skill-tag">Python</span>
                <span class="skill-tag">Java</span>
                <span class="skill-tag">JavaScript</span>
                <span class="skill-tag">HTML5</span>
                <span class="skill-tag">CSS3</span>
                <span class="skill-tag">C++</span>
                <span class="skill-tag">SQL</span>
                <span class="skill-tag">R</span>
            </div>
        </div>
        
        <div class="skill-category">
            <h3><i class="fas fa-globe"></i> Web Development</h3>
            <div class="skill-tags">
                <span class="skill-tag">React.js</span>
                <span class="skill-tag">Node.js</span>
                <span class="skill-tag">Express.js</span>
                <span class="skill-tag">MongoDB</span>
                <span class="skill-tag">MySQL</span>
                <span class="skill-tag">REST APIs</span>
                <span class="skill-tag">Git</span>
                <span class="skill-tag">Streamlit</span>
            </div>
        </div>
        
        <div class="skill-category">
            <h3><i class="fas fa-chart-bar"></i> Data Analysis</h3>
            <div class="skill-tags">
                <span class="skill-tag">Data Visualization</span>
                <span class="skill-tag">Statistical Analysis</span>
                <span class="skill-tag">Predictive Modeling</span>
                <span class="skill-tag">Feature Engineering</span>
                <span class="skill-tag">Data Cleaning</span>
                <span class="skill-tag">EDA</span>
                <span class="skill-tag">A/B Testing</span>
                <span class="skill-tag">Business Intelligence</span>
            </div>
        </div>
        
        <div class="skill-category">
            <h3><i class="fas fa-tools"></i> Tools & Platforms</h3>
            <div class="skill-tags">
                <span class="skill-tag">VS Code</span>
                <span class="skill-tag">Google Colab</span>
                <span class="skill-tag">GitHub</span>
                <span class="skill-tag">Heroku</span>
                <span class="skill-tag">AWS</span>
                <span class="skill-tag">Docker</span>
                <span class="skill-tag">Tableau</span>
                <span class="skill-tag">Power BI</span>
            </div>
        </div>
        
        <div class="skill-category">
            <h3><i class="fas fa-users"></i> Soft Skills</h3>
            <div class="skill-tags">
                <span class="skill-tag">Leadership</span>
                <span class="skill-tag">Mentoring</span>
                <span class="skill-tag">Problem Solving</span>
                <span class="skill-tag">Team Collaboration</span>
                <span class="skill-tag">Project Management</span>
                <span class="skill-tag">Communication</span>
                <span class="skill-tag">Adaptability</span>
                <span class="skill-tag">Critical Thinking</span>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Projects Section
st.markdown("""
<section id="projects" class="section">
    <h2 class="section-title">Featured Projects</h2>
    <div class="projects-grid">
        
        <div class="project-card">
            <div class="project-content">
                <h3 class="project-title">Crop Yield Prediction System</h3>
                <div class="project-meta">
                    <span><i class="fas fa-calendar"></i> 2024</span>
                    <span><i class="fas fa-code"></i> Machine Learning</span>
                    <span><i class="fas fa-globe"></i> Live Demo</span>
                </div>
                <p class="project-description">
                    Advanced ML system that predicts crop yields with 92% accuracy using environmental factors, 
                    historical data, and weather patterns. Built with ensemble methods and feature engineering 
                    techniques to help farmers optimize their agricultural decisions.
                </p>
                <ul class="project-highlights">
                    <li><strong>92% prediction accuracy</strong> using Random Forest and XGBoost models</li>
                    <li><strong>Real-time weather integration</strong> for dynamic predictions</li>
                    <li><strong>Interactive dashboard</strong> with Streamlit for user-friendly access</li>
                    <li><strong>Comprehensive data analysis</strong> of 10+ environmental factors</li>
                    <li><strong>Scalable architecture</strong> supporting multiple crop types</li>
                </ul>
                <a href="https://crop-yield-prediction-system.streamlit.app/" target="_blank" class="project-link">
                    <i class="fas fa-external-link-alt"></i>
                    View Live Demo
                </a>
            </div>
        </div>
        
        <div class="project-card">
            <div class="project-content">
                <h3 class="project-title">Student Performance Analytics</h3>
                <div class="project-meta">
                    <span><i class="fas fa-calendar"></i> 2024</span>
                    <span><i class="fas fa-code"></i> Data Science</span>
                    <span><i class="fas fa-globe"></i> Live Demo</span>
                </div>
                <p class="project-description">
                    Comprehensive analytics platform that analyzes student performance patterns and provides 
                    actionable insights for educational improvement. Features predictive modeling for early 
                    intervention and personalized learning recommendations.
                </p>
                <ul class="project-highlights">
                    <li><strong>Predictive modeling</strong> for at-risk student identification</li>
                    <li><strong>Interactive visualizations</strong> showing performance trends</li>
                    <li><strong>Statistical analysis</strong> of factors affecting academic success</li>
                    <li><strong>Automated reporting</strong> system for educators</li>
                    <li><strong>Data-driven insights</strong> for curriculum optimization</li>
                </ul>
                <a href="https://student-performance-analytics.streamlit.app/" target="_blank" class="project-link">
                    <i class="fas fa-external-link-alt"></i>
                    View Live Demo
                </a>
            </div>
        </div>
        
        <div class="project-card">
            <div class="project-content">
                <h3 class="project-title">Heart Disease Prediction Model</h3>
                <div class="project-meta">
                    <span><i class="fas fa-calendar"></i> 2024</span>
                    <span><i class="fas fa-code"></i> Healthcare AI</span>
                    <span><i class="fas fa-globe"></i> Live Demo</span>
                </div>
                <p class="project-description">
                    AI-powered healthcare application that predicts heart disease risk using patient medical data. 
                    Implements multiple ML algorithms with feature selection and cross-validation for reliable 
                    medical predictions.
                </p>
                <ul class="project-highlights">
                    <li><strong>High accuracy prediction</strong> using ensemble methods</li>
                    <li><strong>Medical data preprocessing</strong> and feature engineering</li>
                    <li><strong>Risk assessment visualization</strong> for healthcare professionals</li>
                    <li><strong>Model interpretability</strong> with SHAP values</li>
                    <li><strong>Clinical validation</strong> with medical datasets</li>
                </ul>
                <a href="https://heart-disease-prediction-model.streamlit.app/" target="_blank" class="project-link">
                    <i class="fas fa-external-link-alt"></i>
                    View Live Demo
                </a>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Experience Section
st.markdown("""
<section id="experience" class="experience">
    <div class="section">
        <h2 class="section-title">Experience & Leadership</h2>
        <div class="experience-grid">
            
            <div class="experience-card">
                <h3 class="experience-title">Machine Learning Engineer</h3>
                <div class="experience-company">Freelance & Personal Projects</div>
                <p class="experience-description">
                    Developed and deployed multiple ML models with high accuracy rates, focusing on real-world 
                    applications in agriculture, healthcare, and education. Built end-to-end ML pipelines from 
                    data collection to model deployment, achieving consistent 90%+ accuracy across different domains.
                </p>
            </div>
            
            <div class="experience-card">
                <h3 class="experience-title">Programming Mentor</h3>
                <div class="experience-company">Community Leadership</div>
                <p class="experience-description">
                    Mentored 40+ students in programming fundamentals, web development, and data science concepts. 
                    Conducted workshops on Python, machine learning, and project development, helping students 
                    transition from beginners to confident developers with practical skills.
                </p>
            </div>
            
            <div class="experience-card">
                <h3 class="experience-title">Full-Stack Developer</h3>
                <div class="experience-company">Academic & Personal Projects</div>
                <p class="experience-description">
                    Designed and developed responsive web applications using modern technologies like React, 
                    Node.js, and Python. Created user-friendly interfaces with focus on performance optimization 
                    and seamless user experience across multiple platforms and devices.
                </p>
            </div>
            
            <div class="experience-card">
                <h3 class="experience-title">Data Analysis Specialist</h3>
                <div class="experience-company">Research & Analytics Projects</div>
                <p class="experience-description">
                    Performed comprehensive data analysis on large datasets, extracting actionable insights 
                    through statistical modeling and visualization techniques. Specialized in predictive analytics, 
                    trend analysis, and creating data-driven recommendations for decision making.
                </p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<section id="contact" class="contact">
    <div class="section">
        <h2 class="section-title">Get In Touch</h2>
        
        <div class="contact-grid">
            <div class="contact-item">
                <i class="fas fa-envelope"></i>
                <h3>Email</h3>
                <p>swethamurugesan2110@gmail.com</p>
            </div>
            
            <div class="contact-item">
                <i class="fas fa-phone"></i>
                <h3>Phone</h3>
                <p>+91 7358749978</p>
            </div>
            
            <div class="contact-item">
                <i class="fab fa-linkedin"></i>
                <h3>LinkedIn</h3>
                <p>Connect with me professionally</p>
            </div>
            
            <div class="contact-item">
                <i class="fab fa-github"></i>
                <h3>GitHub</h3>
                <p>Check out my code repositories</p>
            </div>
        </div>
        
        <div class="contact-links">
            <a href="mailto:swethamurugesan2110@gmail.com" class="contact-btn">
                <i class="fas fa-envelope"></i>
                Send Email
            </a>
            <a href="https://linkedin.com/in/swetha-t-0a3a64252" target="_blank" class="contact-btn">
                <i class="fab fa-linkedin"></i>
                LinkedIn Profile
            </a>
            <a href="tel:+917358749978" class="contact-btn">
                <i class="fas fa-phone"></i>
                Call Now
            </a>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<footer class="footer">
    <p>&copy; 2024 Swetha T. All rights reserved. Built with passion for innovation and excellence.</p>
</footer>
""", unsafe_allow_html=True)

# JavaScript for interactions
st.markdown("""
<script>
// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Header background change on scroll
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (window.scrollY > 100) {
        header.style.background = 'rgba(10, 10, 10, 0.98)';
        header.style.boxShadow = '0 2px 20px rgba(59, 130, 246, 0.2)';
    } else {
        header.style.background = 'rgba(10, 10, 10, 0.95)';
        header.style.boxShadow = 'none';
    }
});

// Animate stats counter
function animateStats() {
    const stats = document.querySelectorAll('.stat-number');
    stats.forEach(stat => {
        const target = parseFloat(stat.innerText);
        let current = 0;
        const increment = target / 100;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            stat.innerText = current % 1 === 0 ? current : current.toFixed(1);
        }, 20);
    });
}

// Trigger stats animation when in view
const observerOptions = {
    threshold: 0.5,
    rootMargin: '0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateStats();
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

const statsSection = document.querySelector('.stats');
if (statsSection) {
    observer.observe(statsSection);
}

// Add loading animation for project links
document.querySelectorAll('.project-link').forEach(link => {
    link.addEventListener('click', function(e) {
        if (this.href.includes('streamlit.app')) {
            const originalText = this.innerHTML;
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
            setTimeout(() => {
                this.innerHTML = originalText;
            }, 3000);
        }
    });
});
</script>
""", unsafe_allow_html=True)
