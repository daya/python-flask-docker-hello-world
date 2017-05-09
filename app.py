import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    app_name = os.getenv('APP_NAME', "Flask")
    return "Hello from %s" % app_name


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.getenv("FLASK_PORT", 5000)))
