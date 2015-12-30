from email_later import db

class Email(db.Model):
    __tablename__ = 'email'
    id = db.Column(db.Integer, primary_key = True)
    event_id = db.Column(db.Integer)
    email_subject = db.Column(db.String(80))
    email_content = db.Column(db.UnicodeText)
    send_to = db.Column(db.String(80))
    timestamp = db.Column(db.String)
    is_sent = db.Column(db.Boolean, default = False)