
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 

from_email = "sunyang1994702@yahoo.co.jp"
pwd = "" 

to_email = "ounann_521@yahoo.co.jp"
smtp_server = "smtp.mail.yahoo.co.jp"

 
# write text content you want send.
message = MIMEText('Python email sending test...', 'plain', 'utf-8')
message['From'] = Header("Mail System", 'utf-8')   # name a sender
message['To'] =  Header("Test User", 'utf-8')        # name a receiver
 
subject = 'Python SMTP mail'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP(smtp_server, 587)
    smtpObj.login(from_email, pwd)
    smtpObj.sendmail(from_email, to_email, message.as_string())
    smtpObj.quit()
    print("email sending successfully!")
except smtplib.SMTPException:
    print("Error: can not send email")
    print(smtplib.SMTPException)
