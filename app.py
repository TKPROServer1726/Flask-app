from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def fhfjks():
  return request.remote_addr

app.run(host='0.0.0.0',port=9927)
