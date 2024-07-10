from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def staticFileDisplay():
    return render_template("StaticFile.html")

app.run()