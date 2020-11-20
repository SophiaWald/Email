import email, smtplib, ssl

from email import encoders

from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465 #port for ssl
smtp_server = "smtp.gmail.com"

subject = "test" #subject of the email
sender_email = "pythontest20.11.2020@gmail.com" #emailaddress from sender
receiver_email = "sophia_waldburger@aol.com" #emailaddress from receiver
password = open("password.txt","r") #opening the password textfile
pwd=password.read() #reading password

message = MIMEMultipart() 
message["Subject"] = subject 
message["From"] = sender_email
message["To"] = receiver_email
message["Bcc"] = receiver_email

file = "photo.jfif" #attached file

with open(file, "rb") as attachment: #attaching the file
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    
encoders.encode_base64(part) #encodes file as ASCII characters 
part.add_header("Content-Disposition", f"attachment; filename= {file}") #having the filename shown as the attachement

html = """\ #message in html
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       I'm sending you an attachement!
       Bye!
    </p>
  </body>
</html>
"""

text = MIMEText(html, "html") #converting html text to MIMEText
message.attach(text) #attach html text
message.attach(part) #attach attachement

context = ssl.create_default_context()
server = smtplib.SMTP_SSL(smtp_server, port, context=context)
server.login(sender_email, pwd)
server.sendmail(sender_email, receiver_email, message.as_string())