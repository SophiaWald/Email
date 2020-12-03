import requests #to request the weather data

import json  #to format the weather data
import smtplib, ssl #for the email
from email.mime.text import MIMEText #to attach text
from email.mime.multipart import MIMEMultipart #to structure the subject,from,to,Bcc

port = 465 #port for gmail
smtp_server = "smtp.gmail.com" #used emailserver

subject = "Temperatur" #subject of the email
sender_email = "?" #emailaddress from sender
receiver_email = "?" #emailaddress from receiver
#The passwort has to be written in an additional textfile named "password.txt"
password = open("password.txt","r") #opening the password textfile 
pwd=password.read() #reading password

message = MIMEMultipart() #structering the Subject, From, To, Bcc
message["Subject"] = subject 
message["From"] = sender_email
message["To"] = receiver_email
message["Bcc"] = receiver_email

api_key = "9b4d9ed267c1131a59b12786bf68ba88" #my API Key

lat = "47.5584" #coordinates of Basel (Switzerland) u can put any coordinates

lon = "7.5733"

url = "http://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key) #URL with inserted api_key,latitude and longitude


response = requests.get(url) #requesting data from the website

data = json.loads(response.text) #getting the data 
current_temp = data["current"]["temp"] #variable for the current temperature in Basel

if current_temp > 30: #If its 30 degrees celsius or higher the following message will get send out
    html = """ 
    <html>
      <body>
        <p>Hi,<br>
           It's so warm today!<br>
           You should go outside and enjoy the weather!
           Have fun!
        </p>
      </body>
    </html>
    """
elif current_temp > 10: #If its 10 degrees celsius or higher the following message will get send out
    html = """ 
    <html>
      <body>
        <p>Hi,<br>
           You'll need a jacket today!<br>
           Bye!
        </p>
      </body>
    </html>
    """
else: #If the temperature is below 10 degrees, this message will get send out
    html = """ 
    <html>
      <body>
        <p>Hi,<br>
           It's freezing outside!<br>
           You might wanna stay home today.
           Bye!
        </p>
      </body>
    </html>
    """

text = MIMEText(html, "html") #converting html text to MIMEText
message.attach(text) #attach the right html text to the message

context = ssl.create_default_context() #starting a secure smtp connection
server = smtplib.SMTP_SSL(smtp_server, port, context=context)
server.login(sender_email, pwd) #logging into the server
server.sendmail(sender_email, receiver_email, message.as_string()) #sending email