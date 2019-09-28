from flask import Flask, jsonify, request
import swatcher

app = Flask(__name__)


@app.route('/')
def hello_world():
  swatch_result = swatcher.swatch_url(request.args['url'])
  return swatch_result

if __name__ == '__main__':
  app.run()
