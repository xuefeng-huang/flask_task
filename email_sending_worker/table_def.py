from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Email(Base):
    """email database definition"""
    __tablename__ = 'email'
    id = Column(Integer, primary_key = True)
    event_id = Column(Integer)
    email_subject = Column(String(80))
    email_content = Column(Text)
    send_to = Column(String(80))
    timestamp = Column(DateTime)
    is_sent = Column(Boolean)
    
    def __init__(self, event_id, email_subject, email_content, send_to, timestamp):
        self.event_id = event_id
        self.email_subject = email_subject
        self.email_content = email_content
        self.send_to = send_to
        self.timestamp = timestamp