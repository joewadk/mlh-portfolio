import os
import datetime
from peewee import *
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)
mydb=MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                   user=os.getenv("MYSQL_USER"),
                   password=os.getenv("MYSQL_PASSWORD"),
                   host=os.getenv("MYSQL_HOST"),
                   port=int(os.getenv("MYSQL_PORT", 3306))
)
print(mydb)

#class def for db
class TimelinePost(Model):
    name=CharField()
    email=CharField()
    content=TextField()
    created_at=DateTimeField(default=datetime.datetime.now)


    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])


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

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

#timeline posts
@app.route('/api/timeline', methods=[ 'POST'])
def post_timeline():
    name = request.form.get('name')
    email = request.form.get('email')
    content = request.form.get('content')
    
    #input validation, throws 400 if any field is empty
    if not name or not email or not content:
        return {'error': 'All fields are required'}, 400

    post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(post)

@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    return {'posts': [model_to_dict(post) for post in TimelinePost.select().order_by(TimelinePost.created_at.desc())]}


@app.route('/api/timeline', methods=['DELETE'])
def delete_last_timeline():
    last_post = TimelinePost.select().order_by(TimelinePost.created_at.desc()).first()

    if last_post: #throwing errors for success and failure to delete
        last_post.delete_instance()
        return {'message': 'last post deleted', 'deleted': model_to_dict(last_post)}, 200
    else:
        return {'error': 'No posts to delete'}, 404
