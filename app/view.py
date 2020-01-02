from app import app
from flask import request, redirect, url_for, render_template, flash
from models.models import bulletin_board
from models.database import db

@app.route('/')                                   
def show_entry():
    result = bulletin_board.query.order_by(bulletin_board.id.desc()).all()
#    return "Hello World!"
    return render_template('show_entries.html', entries=result)

@app.route('/add', methods=['POST'])
def add_entry():
    entry = bulletin_board(
            body=request.form['body']
            )
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entry'))
