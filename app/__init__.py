"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch12sk8rddl13a53f92g-a.oregon-postgres.render.com",
        database="todo_epkl",
        user="todo_epkl_user",
        password="K0EVEoqFyfAEnLCvTkxWFtcKxd6QbSvn")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

