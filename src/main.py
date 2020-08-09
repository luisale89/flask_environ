import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from models import db, User


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
MIGRATE = Migrate(app, db)
db.init_app(app)


@app.route("/")
def home():
    response_body = {
        "msg": "Hola a Todos, JSON msg"
    }

    return jsonify(response_body), 200

@app.route("/webview")
def web():
    return '<h1>Hola a todos. Vista WEB del Sitio</h1>'

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)