# Email

>With this code you can send an email with an attachment. 
The attachement is in this case a jfif file but you can send whatever type of file you want.
The text is written in html.
The password has to be written in the password textfile to be able to login and send the email.
To structure the email and to attach the file to the text I imported MIMEBase, -Text, and Multipart.
I used SMTP to connect to the emailserver and secured the connection with SSL.
The port 465 is for the Gmailserver, so if you have a different email client you have to change the port.
