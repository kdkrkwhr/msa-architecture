from flask import Flask, request
from flask_restx import Api
from flask_cors import CORS
import py_eureka_client.eureka_client as eureka_client
import crawling
import config.server_config as server

app = Flask(__name__)
api = Api(app)
CORS(app)

eureka_client.init(eureka_server=server.EUREKA_SERVER,
                   app_name=server.SERVICE_NAME,
                   instance_host=server.SERVICE_HOST,
                   instance_port=server.SERVICE_PORT)

@app.route("/craw/url", methods=['GET'])
def get_crawling_url():
  return crawling.crawler('https://github.com/kdkrkwhr')

@app.route("/craw/get_data", methods=['POST'])
def post_crawling_data():
  params = request.get_json()
  return crawling.crawler_parsing(params['url'], params['tag'])

@app.route("/craw/test", methods=['GET'])
def test():
  args = request.args
  param = args['param']
  return {"message" : "Hi", "param" : param}

if __name__ == "__main__": 
  app.run(host=server.SERVICE_HOST, port=server.SERVICE_PORT, debug=True)
