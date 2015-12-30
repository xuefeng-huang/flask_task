from email_later import app
from flask import render_template, redirect, url_for
from .form import EmailForm

@app.route('/')
@app.route('/index')
def index():
    return 'hello!'
    
@app.route('/save_emails', methods = ['GET', 'POST'])
def save_email():
    form = EmailForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('send_email.html', form = form)
    
@app.route('/success')
def success():
    return 'success'