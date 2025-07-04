from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)
@app.route('/api/hobbies', methods=['GET'])
def hobbies():
    return jsonify({'Video Games': ['I love playing video games, especially RPGs and strategy games. Some of my favorite games are Doom Eternal and Hollow Knight.'],
                    'Model Kits': ['I enjoy building model kits, especially Gundam models. It’s a great way to relax and express creativity.'],
                    'PC Building': ['I have a passion for building and upgrading PCs. I love the challenge of optimizing performance and aesthetics.'],})

@app.route('/api/education', methods=['GET'])
def education():
    return jsonify({'leaving this empty': 'will merge with pr'
        

    })

