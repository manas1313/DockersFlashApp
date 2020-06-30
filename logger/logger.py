# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 00:09:44 2020

@author: routm1
"""

import logging
import logging.config



logging.config.fileConfig(fname = 'log.conf', disable_existing_loggers = False)

loggerr = logging.getLogger(__name__)
loggerr = logging.getLogger ('applog')
loggerr.setLevel(logging.INFO)

