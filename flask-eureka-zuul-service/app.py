from flask import Flask, request
from flask_restx import Api
from flask_cors import CORS
import py_eureka_client.eureka_client as eureka_client
import config, crawling


app = Flask(__name__)
api = Api(app)
CORS(app)

eureka_client.init(eureka_server=config.EUREKA_SERVER,
                   app_name=config.SERVICE_NAME,
                   instance_host=config.SERVICE_HOST,
                   instance_port=config.SERVICE_PORT)

@app.route("/craw/url", methods=['GET'])
def get_crawling_url():
  return crawling.crawler()

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
  app.run(host=config.SERVICE_HOST, port=config.SERVICE_PORT, debug=True)
