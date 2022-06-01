from flask import render_template

from app import app
from models.order_list import *


@app.route("/")
def index():
    return render_template("index.html")
