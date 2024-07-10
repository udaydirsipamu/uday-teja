from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "GET":
        return render_template("Login1.html", error=error)
    if request.method == "POST":
        if request.form["userName"] == "Uday" and request.form["pwd"] == "Admin":
            return render_template("ValidUser1.html")
        else:
            error = "Invalid credentials.. Pls check your id and password"
            return render_template("Login1.html", error=error)


app.run()