# ************************************************
#  (c) 2019-2021 Nurul-GC                        *
# ************************************************

import os
basedir = os.path.abspath(os.path.dirname(__file__)+'/database')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ANGOLACKERS_API'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
