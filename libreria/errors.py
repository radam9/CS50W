from flask import render_template
from libreria import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title='404 - Not Found'), 404
