from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/hobbies')
def hobbies():
    return render_template("hobbies.html")
if __name__ == "__main__":
    app.run(debug=True)

