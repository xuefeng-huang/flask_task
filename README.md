#start server: 
python manage.py runserver

#checking email to be sent
set cron job to run **send_mandrill.py** every minute inside **email_sending_worker** folder  
run **email_sending_worker.py** for python native email if mandrill not available

check out the [code](https://ide.c9.io/xuefeng_huang/send_email_later_flask) on Cloud9