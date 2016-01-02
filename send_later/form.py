from flask_wtf import Form
from wtforms import validators, StringField, TextAreaField
from wtforms.fields.html5 import EmailField

class EmailForm(Form):
    event_id = StringField('event id', [validators.Required()])
    email_subject = StringField('subject', [validators.Required()])
    email_content = TextAreaField('content', [validators.Required()])
    send_to = EmailField('Email', [validators.Required()])
    timestamp = StringField('time to send(ex. Jan 01 2016 14:42)', [validators.Required()])
   