import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

CSV_FILE_PATH="C://Kasi/employee_data.xlsx"
sender = 'admin@example.com'
receivers = ['trainingsinfo77@gmail.com','kasi.yedumati@gmail.com']
msg= MIMEMultipart()
body_text=MIMEText("Please find csv file")
msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'trainingsinfo77@gmail.com'
msg.attach(body_text)
port = 1025

with open(CSV_FILE_PATH,'r') as csvfile:
    msg.attach(MIMEApplication(csvfile.read(),name="employeecsv"))
try:
    with smtplib.SMTP('localhost', port) as smptpserver:
        #server.login('username', 'password')
        smptpserver.sendmail(sender, receivers, msg.as_string())
        smptpserver.quit()
        print("Successfully sent email")
except SMTPException:
    print("Error while sending...")

