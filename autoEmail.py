#  Objective: Send an automated email using Gmail


import smtplib
from email.mime.text import MIMEText

#smtplib for sending emailing
smtpServer= "smtp.gmail.com"
port = 587
sendersEmail="xyz@gmail.com"
receiverEmail= "abc@gmail.com"
message = "this is a automated message xyz syed to abc  "

#MIMEText for creating Email structure
msg=MIMEText(message)
msg['Subject'] = "Automated Email"
msg['From'] = sendersEmail
msg['To'] = receiverEmail

#opening a connection and auto closing after sending email
try:

    with smtplib.SMTP(smtpServer, port) as server:
        server.starttls()

        #As user has 2FA enable, use "App password" from gmail
        password = input("enter your password : ") #use "app password" for security
        server.login(sendersEmail, password)
        server.sendmail(sendersEmail, [receiverEmail], msg.as_string())
except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email or app password.")
except Exception as e:
        print(f"Something went wrong: {e}")


