from . import login
from flask import render_template, request, jsonify


@login.route('/signup')
def home():
    print("signup")
    return "hola cliente"


@login.route('/add', methods=['POST'])
def add():
    body = request.get_json()
    if body is None:
        return print("no data"), 400
    else:
        return "ok", 200