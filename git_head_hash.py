# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 04:41:28 2020

@author: routm1
"""

import subprocess

process = subprocess.Popen(['git', 'rev-parse', 'HEAD'], shell=False, stdout=subprocess.PIPE)
git_head_hash = process.communicate()[0].strip()

