import smtplib
from email.mime.text import MIMEText

sender = 'trainingsinfo77@gmail.com'
receivers = ['trainingsinfo77@gmail.com','kasi.yedumati@gmail.com']
port = 1025
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'trainingsinfo77@gmail.com'


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.ehlo()
    server.login(sender, '6302193992')
    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")
# except SMTPException:
#     print("Error while sending...")

# Converting Database table to CSV File and send that csv file to your mail ID
# It will refund within 24 hours

