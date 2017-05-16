import os
from flask import Flask, abort, request
from subprocess import call, PIPE, Popen

app = Flask(__name__)

def host_name():
  return Popen("hostname", stdout=PIPE).stdout.read()

@app.route("/")
def hello():
  app_name = os.getenv('APP_NAME', "Flask")
  app_desc = os.getenv('APP_DESC', "Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions")

  return "Hello from %s.<br/> Data: %s.<br/> Description: %s.<br/> ContainerID: %s" % (
    app_name,
    request.query_string,
    app_desc,
    host_name()
    )

@app.route("/msg", methods=["POST", "GET"])
def msg():
  print("Args %s, %s", (request.args.get('name'), request.args.items))
  return "MSG Received: %s" % (request.data if request.data else request.query_string)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.getenv("FLASK_PORT", 5000)))

