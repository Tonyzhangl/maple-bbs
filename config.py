#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2017 kirago
# File Name: config.py
# Author: kirago
# Email: zhangl910201@gmail.com
# Created: 2017-07-21 17:00:00 (CST)
# Description:
# **************************************************************************
from datetime import timedelta
from os import path, pardir

DEBUG = True
SECRET_KEY = 'secret key'
SECURITY_PASSWORD_SALT = 'you will never guess'
SECRET_KEY_SALT = 'you will never guess'

# avatar upload directory
AVATAR_FOLDER = path.join(path.abspath(path.dirname(__file__)), 'avatar')
# avatar generate range
AVATAR_RANGE = [122, 512]

# for development use localhost:5000
# for production use xxx.com
# SERVER_NAME = 'localhost:5000'

# remember me to save cookies
PERMANENT_SESSION_LIFETIME = timedelta(days=3)
REMEMBER_COOKIE_DURATION = timedelta(days=3)
ONLINE_LAST_MINUTES = 5

# You want show how many topics per page
PER_PAGE = 12

# Use cache
CACHE_TYPE = 'null'
CACHE_DEFAULT_TIMEOUT = 60
CACHE_KEY_PREFIX = 'cache:'
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = '6379'
CACHE_REDIS_PASSWORD = 'your password'
CACHE_REDIS_DB = 2

# Redis setting
REDIS = {'db': 1, 'password': 'your password', 'decode_responses': True}

# some middleware
MIDDLEWARE = ['forums.common.middleware.GlobalMiddleware',
              'forums.common.middleware.OnlineMiddleware']

# Mail such as qq
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "your email"
MAIL_PASSWORD = "your password"
MAIL_DEFAULT_SENDER = 'your email'
# MAIL_SUPPRESS_SEND = True

# Log,if SEND_LOGS is True when web app has some error happen(500)
# the email will be sent to RECEIVER
SEND_LOGS = True
RECEIVER = ["yourname@gmail.com"]
INFO_LOG = "info.log"
ERROR_LOG = "error.log"
SERVER_NAME = 'localhost:5000'
SUBDOMAIN = {'forums': True, 'docs': True}

# Sql
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/your_db'

MSEARCH_INDEX_NAME = 'whoosh_index'
MSEARCH_BACKEND = 'whoosh'
# SQLALCHEMY_ECHO = True
# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
# SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'

# Locale
LANGUAGES = {'en': 'English', 'zh': 'Chinese'}
SITE = {'title': 'Honmaple', 'description': '爱生活，更爱自由', 'avatar': ''}
