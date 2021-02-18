import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender = 'from@runoob.com'
receivers = ['sunyang1994702@yahoo.co.jp']  # set a receiver mail address
 
# write text content you want send.
message = MIMEText('Python email sending test...', 'plain', 'utf-8')
message['From'] = Header("Mail System", 'utf-8')   # name a sender
message['To'] =  Header("Test User", 'utf-8')        # name a receiver
 
subject = 'Python SMTP mail test'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("email sending successfully!")
except smtplib.SMTPException:
    print("Error: can not send email")