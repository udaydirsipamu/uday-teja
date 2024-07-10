from flask import Flask
app = Flask(__name__)

@app.route ('/')
def welcome ():
    return "Hey,Welcome to the land of Python Server.."
app.run()
