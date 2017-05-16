import os
from flask import Flask, abort, request

app = Flask(__name__)

@app.route("/")
def hello():
    app_name = os.getenv('APP_NAME', "Flask")
    return "Hello from %s. Data: %s" % (app_name, request.query_string)

@app.route("/msg", methods=["POST", "GET"])
def msg():
  print("Args %s, %s", (request.args.get('name'), request.args.items))
  return "MSG Received: %s" % (request.data if request.data else request.query_string)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.getenv("FLASK_PORT", 5000)))
