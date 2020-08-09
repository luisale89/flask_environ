import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route("/")
def home():
    return '<h1>Hello World</h1>'


if __name__ == '__main__':
    app.run()