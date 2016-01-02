from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Email
from datetime import datetime
import mandrill, os

engine = create_engine('sqlite:///../email.db')
Session = sessionmaker(bind=engine)
session = Session()

emails_not_sent = session.query(Email).filter(Email.is_sent==False).all() #get all email not sent yet

mandrill_client = mandrill.Mandrill(os.getenv('API_KEY'))

for m in emails_not_sent:
    if m.timestamp <= datetime.now():
        #send mail if time reaches
        try:
            message = {
             'from_email': 'timhxf@gmail.com',
             'from_name': 'Huang xuefeng',
             'subject': m.email_subject,
             'text': m.email_content,
             'to': [{'email': m.send_to,
                     'type': 'to'}]
             }
             
            result = mandrill_client.messages.send(message=message, async=False)
            
        
        except mandrill.Error as e:
            print('A mandrill error occurred: {0} - {1}'.format(e.__class__, e))
            raise    
        
        #set is_sent flag
        m.is_sent = True
        
session.commit() #update all record already sent