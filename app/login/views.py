from . import login
from flask import render_template, request, jsonify
from app.models import User
from app import db
from bcrypt import gensalt, hashpw


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
            for item in body:
                if body.get(item) is not "":
                    pass
                else:
                    return jsonify(
                        message='missing value in 1 or more parameters',
                        status=400
                    )
            # grabs all values from dictionary and store it
            if User.query.filter_by(email=body['email']).first() and User.query.filter_by(username=body['username']).first():
                return jsonify(
                    message="already existis username or email",
                    status=400
                )
            else:

                password = body['password_hash']
                h = hashpw(password.encode(), gensalt())
                body['password_hash'] = h
                user = User(**body)
                db.session.add(user)
                user = User(**body)
                db.session.add(user)
                try:
                    db.session.commit()
                except db.error as e:
                    db.session.rollback()

            return jsonify(
                message="User Added",
                status=200
            )

        else:
            return jsonify(message="no es post")
    else:
        return jsonify(
            message="not content",
            status=400
        )
