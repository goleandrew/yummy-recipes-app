'''File for initialzing the app'''
from flask import Flask

# Let's initialize the app

app = Flask(__name__, instance_relative_config=True)

#We load the view
from app import views

#Now we load the config file

app.config.from_object('config')
