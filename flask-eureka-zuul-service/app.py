from flask import Flask, request
from flask_restx import Api
from flask_cors import CORS
import py_eureka_client.eureka_client as eureka_client
import config

app = Flask(__name__)
api = Api(app)
CORS(app)

eureka_client.init(eureka_server=config.EUREKA_SERVER,
                   app_name=config.SERVICE_NAME,
                   instance_host=config.SERVICE_HOST,
                   instance_port=config.SERVICE_PORT)

@app.route("/python/get", methods=['GET'])
def get_api():
  args = request.args
  param = args['param']
  return {"message" : "Hi", "param" : param}

@app.route("/python/hello/<string:name>", methods=['GET'])
def hello_name(name):
  return {"message" : "Welcome, %s" % name}

if __name__ == "__main__": 
  app.run(host=config.SERVICE_HOST, port=config.SERVICE_PORT, debug=True)
