from LearningPathData import learning_paths
from Path_generator import path_generator
from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy
from app import app, db  

for i, learning_path in enumerate(learning_paths, start=1):
    image_name = f"learning_path_{i}.png"
    path_generator(learning_path, image_name)
