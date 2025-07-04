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
    return render_template('hobbies.html', hobbies=hobbies, current_year=current_year)