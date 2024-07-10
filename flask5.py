from flask import Flask
app=Flask(__name__)

@app.route('/WelcomeName')
@app.route('/WelcomeName/<name>')
def welcomeName(name='Uday'):
    str ='Welcome ' + name
    return str
app.run()