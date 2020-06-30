# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 01:55:05 2020

@author: routm1
"""
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("environment.DevelopmentConfig")
port = app.config["PORT"]
app.config["DEBUG"] = False

server_name = "127.0.0.1:" + port
app.config["SERVER_NAME"] = server_name
#app.config['SECRET_KEY'] = 'dadjahgdjagjdgsjkt63827fbg'

from myapp import view

