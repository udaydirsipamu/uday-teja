from flask import Flask
app=Flask(__name__)
@app.route('/sayHello')
def sayHello():
    return "Hello from Python Flask Server..This is plain text"
@app.route('/SayHelloInHTML')
def SayHelloInHTML():
    return "<h1>Hello,Welcome from Python  Flask server..returning data in HTML format </h1>"
@app.route('/jsonData')
def jsonData():
    data={
        "id" : 101,
        "title" : "Introduction to Flask",
        "author" : "By Uday",
        "cost" : 350
    }
    return data
app.run()