from flask import Flask
from app import create_app, db
from flask_migrate import Migrate
from dotenv import load_dotenv
import os


""" Load environment variable from .env file"""
load_dotenv()

""" Create the app instance"""
app = create_app(os.getenv('FLASK_ENV', 'development'))

""" Initialize flask_Migrate """
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Hello, BullStreet is coming!"

print("Starting Flask app...")


if __name__ == '__main__':
    app.run(debug=True)