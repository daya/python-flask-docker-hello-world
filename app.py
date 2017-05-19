import os
from flask import Flask, abort, request
from subprocess import call, PIPE, Popen

app = Flask(__name__)

def host_name():
  return Popen("hostname", stdout=PIPE).stdout.read()

def client_cert():
  return request.headers.get('X_SSL_CLIENT_CERT')

@app.route("/")
def hello():
  print("CLIENT CERT: %s" % client_cert())
  app_name = os.getenv('APP_NAME', "Flask")
  app_desc = os.getenv('APP_DESC', "Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions")
  return "Hello from %s.<br/>\n Data: %s.<br/>\n Description: %s.<br/>\n ContainerID: %s . <br>\n SSL Client Certificate: %s" % (
    app_name,
    request.query_string,
    app_desc,
    host_name(),
    client_cert()
    )

@app.route("/msg", methods=["POST", "GET"])
def msg():
  print("Args %s, %s", (request.args.get('name'), request.args.items))
  return "MSG Received: %s. <br/> ContainerID: %s" % (request.data if request.data else request.query_string, host_name())

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.getenv("FLASK_PORT", 5000)))

