from flask import Flask
from flask import request
app=Flask(__name__)

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='GET':
        return "This is a GET Method"
    elif request.method=='POST':
        return "Given request is POST Method"
app.run()