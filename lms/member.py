from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from lms.db import get_db

bp = Blueprint('member', __name__, url_prefix='/member')

@bp.route('/', methods=['GET'])
def index():
    db = get_db()
    members = db.execute(
        'SELECT id, name'
        ' FROM member'
        ' ORDER BY id ASC'
        ' LIMIT 20;'
    ).fetchall()
    return render_template('member/index.html', members=members)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        name = request.form['name']
        error = None

        if not name:
            error = "Member name required"

        if error:
            flash(error)
        else:
            print(name)
            db = get_db()
            db.execute(
                'INSERT INTO member (name)'
                ' VALUES (?)',
                (name,)
            )
            db.commit()
            return redirect(url_for('member.index'))
    
    return render_template('member/create.html')

