from flask import render_template, jsonify
from libreria import app, db

@app.errorhandler(404)
def not_found_error(error):
    if error.description == None:
        return render_template('404.html', title='404 - Not Found'), 404
    else:
        return jsonify({'message': error.description}), 404
