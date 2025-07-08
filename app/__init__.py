from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("CPF"))

def create_app():
    app = Flask(__name__)
    return app