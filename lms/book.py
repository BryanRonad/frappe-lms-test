from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from lms.db import get_db

bp = Blueprint('book', __name__, url_prefix='/book')

@bp.route('/', methods=['GET'])
def index():
    db = get_db()
    books = db.execute(
        'SELECT id, name, author'
        ' FROM book'
        ' ORDER BY id ASC'
        ' LIMIT 20;'
    ).fetchall()
    return render_template('book/index.html', books=books)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        name = request.form['name']
        author = request.form['author']
        errors = []

        if not name:
            errors.append("Name required")

        if not author:
            errors.append("Author required")

        if len(errors) != 0:
            flash(",".join(errors))     
        else:
            db = get_db()
            db.execute(
                'INSERT INTO book (name, author)'
                ' VALUES (?, ?)',
                (name, author)
            )
            db.commit()
            return redirect(url_for('book.index'))
    
    return render_template('book/create.html')
