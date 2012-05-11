"""The main navas.me app"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
  """Render Website's home page."""
  return render_template('home.html')


@app.errorhandler(404)
def page_not_found(error):
  """Custom 404 page."""
  return render_template('404.html'), 404

if __name__ == '__main__':
  app.run(debug=True)
