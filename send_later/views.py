from email_later import app, db
from flask import render_template, redirect, url_for
from .form import EmailForm
from .models import Email
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    return 'hello!'
    
@app.route('/save_emails', methods = ['GET', 'POST'])
def save_email():
    form = EmailForm()
    
    if form.validate_on_submit():
        time_to_datetime = datetime.strptime(form.timestamp.data, '%b %d %Y %H:%M') #convert string to datetime
        email_obj = Email(form.event_id.data, 
        form.email_subject.data,
        form.email_content.data, 
        form.send_to.data,
        time_to_datetime
        )
        db.session.add(email_obj)
        db.session.commit()
        return redirect(url_for('success'))
        
    return render_template('send_email.html', form = form)
    
@app.route('/success')
def success():
    return 'successfully saved'