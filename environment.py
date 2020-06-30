# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 01:56:38 2020

@author: routm1
"""

class Config(object):
    PORT = '5000'
    LOG_LEVEL = 'CRITICAL'

class DevelopmentConfig(Config):
    PORT = '5736'
    LOG_LEVEL = 'INFO'
    
class TestingConfig(Config):
    PORT = '5002'
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    PORT = '8080'
    LOG_LEVEL = 'ERROR' 
