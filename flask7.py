from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/welcome')
@app.route('/welcome/<name>')
def sayHello(name='New User'):
    return render_template('welcome.html', variableName=name)
app.run()