import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("USER_NAME")
EMAIL_PASS = os.environ.get("USER_PASS")

msg =  EmailMessage()
msg['Subject']= 'Lets do emaling via python'
msg['From'] = EMAIL_ADDRESS
msg['To'] = input('enter your email address:\t')
msg.set_content('lets get it going!')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    
    smtp.send_message(msg)
    
