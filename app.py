"""The main navas.me app"""
from __future__ import with_statement
import time
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from contextlib import closing
from flask import Flask, render_template, request, session, redirect, url_for, abort, g, flash
from werkzeug import check_password_hash, generate_password_hash



app = Flask(__name__)
    

@app.route('/')
def home():
  return render_template('home.html')

                      

@app.errorhandler(404)
def page_not_found(error):
  """Custom 404 page."""
  return render_template('404.html'), 404

if __name__ == '__main__':
  app.run(debug=True)
