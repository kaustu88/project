from flask import render_template, request
from FlaskTemplate import app

@app.route('/')
@app.route('/home')
def home():
   
    name = request.args.get('name')

    return render_template(
        'index.html',
        # Display the name on the website.
        name = name
    )
