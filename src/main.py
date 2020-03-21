import os, re
from flask import Flask, jsonify, request, url_for
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from functools import wraps
from models import (
    db, User
)
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity,
    verify_jwt_in_request, get_jwt_claims, get_raw_jwt, jwt_optional
)
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"
app.config["JWT_SECRET_KEY"] = "encrypt"
app.config["DEBUG"] = True
app.config["ENV"] = "development"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DB_CONNECTION_STRING')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
CORS(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password: 
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"msg": "Email not found"}), 404

    if bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=email)
        data = {
            "access_token": access_token,
            "user": user.serialize(),
            "msg": "success"
        }
        return jsonify(data), 200


@app.route("/signup", methods=["POST"])
def signup():
    #Regular expression that checks a valid email
    ereg = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    #Regular expression that checks a valid password
    preg = '^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$'
    user = User()
    #checking email
    if (re.search(preg, request.json.get('password'))):
        pw_hash = bcrypt.generate_password_hash(request.json.get("password"))
        user.password = pw_hash
    else:
        return "Invalid password format", 400
    #Ask for everything else
    user.fname = request.json.get("fname")
    user.lname = request.json.get("lname")

    db.session.add(user)
    db.session.commit()

    return jsonify({"success": True}), 201


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)