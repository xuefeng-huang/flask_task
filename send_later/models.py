from email_later import db

class Email(db.Model):
    __tablename__ = 'email'
    id = db.Column(db.Integer, primary_key = True)
    event_id = db.Column(db.Integer)
    email_subject = db.Column(db.String(80))
    email_content = db.Column(db.UnicodeText)
    send_to = db.Column(db.String(80))
    timestamp = db.Column(db.DateTime)
    is_sent = db.Column(db.Boolean, default = False)
    
    def __init__(self, event_id, email_subject, email_content, send_to, timestamp):
        self.event_id = event_id
        self.email_subject = email_subject
        self.email_content = email_content
        self.send_to = send_to
        self.timestamp = timestamp