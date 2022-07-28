import smtplib
from email.mime.text import MIMEText

sender = 'admin@example.com'
receivers = ['trainingsinfo77@gmail.com','kasi.yedumati@gmail.com']
port = 1025
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'trainingsinfo77@gmail.com'

try:
    with smtplib.SMTP('localhost', port) as server:
        #server.login('username', 'password')
        server.sendmail(sender, receivers, msg.as_string())
        print("Successfully sent email")
except SMTPException:
    print("Error while sending...")

# Converting Database table to CSV File and send that csv file to your mail ID
# It will refund within 24 hours

