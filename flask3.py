from flask import Flask
app=Flask(__name__)
@app.route('/')
def welcome():
    return "Hey,welcome to the land of python Server.."
@app.route('/hello')
def sayHello():
    return "Hello from Python Server"
@app.route('/displayName/<name>')
def displayName(name):
    return "Hello " + name + ", Welcome to Python server.."
app.run()