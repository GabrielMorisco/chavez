from flask import Flask
app = Flask(_name_)

@app.rout('/')
def hello_world():
  return 'Hello, World!'
