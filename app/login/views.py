from . import login
from flask import render_template, request, jsonify
from app.models import User
from app import db


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
            user = User(**body)
            db.session.add(user)
            db.session.commit()
            User.query.limit(1).all()
            return jsonify(
                message="everything is good",
                status=200
            )

        else:
            return jsonify(message="no es post")
    else:
        return jsonify(
            message="not content",
            status=400
        )
