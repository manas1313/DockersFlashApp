# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 02:13:35 2020

@author: routm1
"""

from myapp import app
from flask import render_template, jsonify, Blueprint
from appenv import infosetup
#import logging
from logger import logger
 
errors = Blueprint('errors', __name__)


@app.route('/')
def index():
    return render_template('home.html')
#    return '<h1>This is the Home Page.</h1>'
       
#@app.route('/template')
#def template():
#    return render_template('home.html')

@app.route('/info', methods=['GET','POST'])
def info(): 
    logger.loggerr.info("Information page called")
    loglevel= logger.loggerr.level
    lg_level =logg_level(loglevel)       
    port = app.config["PORT"]  
    dfr = infosetup.info()
    
    
    appinfo = {"name": dfr['name'], "version" : dfr['version'], "environment": {"service_port" : port, "log_level" : lg_level}}
   
#    resp = json.dumps(appinfo, separators=(',', ': '), indent=2)
    
    return appinfo

#def page_not_found(e):
#  return render_template('404.html'), 404
    
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@errors.app_errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args]
    status_code = error.status_code
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response), status_code

def logg_level(level):   
    
    return 'DEBUG' if level == 10 else 'INFO' if level == 20 else 'WARNING' if level == 30 else 'ERROR' if level == 40 else 'CRITICAL' if level == 50 else 'NOTSET'
    

    