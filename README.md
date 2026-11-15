# Personal Portfolio Website

## About the Project
This is my personal portfolio website, developed using Python and FastAPI as part of my Full Stack Development learning journey.
The website showcases my profile, technical skills, projects, internship experience, and contact information. It also includes a Dark Mode and Light Mode feature that remembers the user's selected theme using cookies.

## Technologies Used
- **Python** – Backend programming
- **FastAPI** – Web framework
- **Jinja2** – HTML templating
- **HTML** – Page structure
- **CSS** – Styling and responsive layout

## Features
- Personal introduction and profile section
- Technical skills showcase
- Projects section with GitHub links
- Internship experience
- Contact section for opportunities
- Dark Mode and Light Mode toggle
- Cookie-based theme preference
- Dynamic current year display

## Project Structure
portfolio/
│
├── main.py
│
├── templates/
│   ├── base.html
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── images/
│       └── profile.jpg
│
└── README.md

### 1. Navigate to the Project Folder

### 2. Create a Virtual Environment
python -m venv venv

### 3. Activate the Virtual Environment
venv\Scripts\activate

### 4. Install Required Libraries
pip install fastapi uvicorn jinja2

### 5. Write the code

### 6. Run the Application
uvicorn main:app --reload

### 7. Open in Browser
Visit:
http://127.0.0.1:8000

## What I Learned
- Creating and handling routes using FastAPI.
- Connecting HTML pages with Jinja2 templates.
- Serving static files such as CSS and images.
- Handling GET and POST requests.
- Working with HTML forms.
- Managing cookies to store user preferences.
- Implementing Dark Mode and Light Mode functionality.
- Understanding frontend and backend integration.
- Organizing a FastAPI project structure.

## Future Improvements
- Add a downloadable resume.
- Improve responsive design for mobile devices.
- Add a contact form with email functionality.
- Deploy the portfolio website online.

⭐ If you find this project useful, feel free to explore the repository!
