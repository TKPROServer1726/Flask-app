from flask import Flask

app = Flask(__name__)

@app.route("/")
def fhfjks():
  return "/"

app.run(host='0.0.0.0',port=9999)
