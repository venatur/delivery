import base64

from . import login
from flask import request, jsonify
from app.models import User
from app import db
from bcrypt import gensalt, hashpw, checkpw
from werkzeug.security import generate_password_hash, check_password_hash


# message handler for return json responses
def msg_handler(message, code):
    return jsonify(message=message, status=code)


@login.route('/signup')
def home():
    print("signup")
    return {'hello', 'world'}


@login.route('/add', methods=['GET', 'POST'])
def add():
    error = None
    # get data from JSON
    body = request.get_json()

    # if data contains something
    if body != error:
        # Verification of POST method
        if request.method == 'POST':
            # bucle for empty values findings
            validation = all(x != "" for x in body.values())
            if validation:
            # compare if username and email exists
                if User.query.filter_by(username=body['username']).first():
                    return msg_handler("username already exists", 400)
                # store body values
                else:
                    password = body['password_hash']
                    #h = hashpw(password.encode('utf-8'), gensalt())
                    h = generate_password_hash(password)
                    body['password_hash'] = h
                    user = User(**body)
                    db.session.add(user)
                    try:
                        db.session.commit()
                    except db.error as e:
                        db.session.rollback()
                return msg_handler("user added", 200)
            else:
                return jsonify(
                    message='missing value in 1 or more parameters',
                    status=400
                )
        else:
            return msg_handler("must be POST method", 400)
    else:
        return msg_handler("no data", 400)


@login.route('/log',methods=['POST'])
def login():
    error = None
    # get data from JSON
    body = request.get_json()

    # if data contains something
    if body != error:
        # Verification of POST method
        if request.method == 'POST':
            # bucle for empty values findings
            validation = all(x != "" for x in body.values())
            if validation:
                username_mod = body['username']
                password_mod = body['password_hash']
                userMatch = User.query.filter_by(username=username_mod).first()
                store_password = userMatch.password_hash

                if userMatch:
                    if check_password_hash(store_password, password_mod ):
                        pswd_match = True
                    else:
                        pswd_match = False

                if userMatch and pswd_match:
                    return msg_handler("user allowed", 200)
                else:
                    return msg_handler("user denied", 400)
            else:
                return msg_handler("missing value in 1 or more parameters", 400)
        else:
            return msg_handler("Must be POST method", 400)
    else:
        return msg_handler("no data", 400)