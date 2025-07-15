import os
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hobbies')
def hobbies():
    hobbies = {
        'Video Games': {
            'descriptions': ['I love playing video games, especially RPGs and strategy games. Some of my favorite games are Doom Eternal and Hollow Knight.'],
            'image': 'https://jawad-stuff.s3.us-east-1.amazonaws.com/hk.jpg'
        },
        'Model Kits': {
            'descriptions': ['I enjoy building model kits, especially Gundam models. It’s a great way to relax and express creativity.'],
            'image': 'https://jawad-stuff.s3.us-east-1.amazonaws.com/gundam.jpg'
        },
        'PC Building': {
            'descriptions': ['I have a passion for building and upgrading PCs. I love the challenge of optimizing performance and aesthetics.'],
            'image': 'https://jawad-stuff.s3.us-east-1.amazonaws.com/pc.jpg'
        }
    }
    from datetime import datetime
    current_year = datetime.now().year
    return render_template('hobbies.html', hobbies=hobbies)

@app.route('/about')
def about():
    from datetime import datetime
    current_year = datetime.now().year
    return render_template('about.html')

@app.route('/education')
def education():
    from datetime import datetime
    current_year = datetime.now().year
    return render_template('education.html')

@app.route('/experience')
def experience():
    experiences = [
        {
            'company': 'Major League Hacking',
            'role': 'MLH Fellow',
            'dates': 'Summer 2025',
            'description': 'Incoming Production Engineering MLH fellow working on open source projects, collaborating with fellows, and building portfolio projects.',
            'image': 'https://jawad-stuff.s3.us-east-1.amazonaws.com/mlh.png'
        },
        {
            'company': 'IPG Health',
            'role': 'Software Developer Intern',
            'dates': '2025',
            'description': 'Built internal tools and improved backend pipelines to support personalized healthcare marketing using NLP and computer vision.',
            'image': 'https://jawad-stuff.s3.us-east-1.amazonaws.com/ipghealth.png'
        },
        {
            'company': 'Emerald Energy',
            'role': 'Software Developer Intern',
            'dates': '2024',
            'description': 'Led backend dev for a chatbot that replaced 200+ manuals, reducing technician setup time using LangChain and vector search.',
            'image': 'https://jawad-stuff.s3.us-east-1.amazonaws.com/emerald_energy_logo.jpg'
        }
    ]
    from datetime import datetime
    current_year = datetime.now().year
    return render_template('experience.html', experiences=experiences)

@app.route('/projects')
def projects():
    projects = [
        {
            'title': 'MLH Portfolio',
            'description': 'A personal portfolio site built for the MLH Fellowship using Flask, featuring dynamic pages for hobbies, education, experience, and more. I have also set up a redeploy script to automatically fetch and add changes from github',
            'image': ''
        }
    ]
    from datetime import datetime
    current_year = datetime.now().year
    return render_template('projects.html', projects=projects)

@app.route('/map')
def map_page():
    import os
    from datetime import datetime
    current_year = datetime.now().year
    globe_api_key = os.environ.get('GLOBE_API_KEY', '')
    return render_template('map.html', current_year=current_year, GLOBE_API_KEY=globe_api_key)  # be suyre to include the maptiler api key in your .env file
