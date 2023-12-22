from flask import Flask, request, render_template

app=Flask(__name__)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name= request.form['name']
        email=request.form['email']
        password=request.form['password']

    return render_template('register.html')
