from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2, dotenv, os
from flask_restx import Api
from flask_cors import CORS
import subprocess  # Import the subprocess module
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
CORS(app, origins='http://127.0.0.1:3000')

dotenv.load_dotenv()
db_url = os.getenv('BOT_DATABASE_URL')

conn = psycopg2.connect(db_url, sslmode='prefer')

# app.config['SQLALCHEMY_DATABASE_URI'] = db_url
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object('chatbot.config.DevelopmentConfig')

db = SQLAlchemy(app)
jwt = JWTManager(app)

from chatbot.routes import *

# Define a function to run the training process
def run_training():
    try:
        # Run the train.py script using subprocess
        subprocess.run(['python', './train.py'])
        print("Training process completed.")
    except Exception as e:
        print(f"Error: {e}")

# Run the training process when the app starts
if __name__ == '__main__':
    run_training()  # Run training when the app starts
    app.run(debug=True)
