from flask import (
    Blueprint, render_template, request, flash
)

from app.db import get_db

bp = Blueprint('mail', __name__, url_prefix="/")

@bp.route('/', methods=['GET'])
def index():
    db, c = get_db()

    c.execute('SELECT * FROM email')
    mails = c.fetchall()

    return render_template('mails/index.html', mails=mails)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        email = request.form.get('email')
        subject = request.form.get('subject')
        content = request.form.get('content')
        errors = []

        if not email:
            errors.append('Email es obligatorio')
        if not subject:
            errors.append('El asunto es obligatorio') 
        if not content:
            errors.append('El contenido es obligatorio')

        if len(errors) == 0:
            pass
        else:
            for error in errors:
                flash(error)
    return render_template('mails/create.html')