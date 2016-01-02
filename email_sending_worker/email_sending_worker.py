from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Email
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import os

engine = create_engine('sqlite:///../email.db')
Session = sessionmaker(bind=engine)
session = Session()

emails_not_sent = session.query(Email).filter(Email.is_sent==False).all() #get all email not sent yet

client = smtplib.SMTP('smtp.mail.yahoo.com', 587)
client.ehlo()
client.starttls()
client.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))

for m in emails_not_sent:
    if m.timestamp <= datetime.now():
        #send email
        msg = MIMEText(m.email_content)
        msg['Subject'] = m.email_subject
        msg['From'] = 'timhxf@gmail.com'
        msg['To'] = m.send_to
        client.sendmail(msg['From'], msg['To'], msg.as_string())
        
        #set is_sent flag
        m.is_sent = True
        
client.quit()
session.commit() #update all record already sent
        
        