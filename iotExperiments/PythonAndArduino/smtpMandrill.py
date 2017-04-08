#Standard smpt module for python to send mail
#Mandrill smpt used to send mail
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(mail):
	msg = MIMEMultipart('alternative')

	msg['Subject'] = mail['subject']
	msg['From'] = mail['fromEmail'] # Your from name and email address
	msg['To'] = mail['toEmail']

	part1 = MIMEText(mail['content'], 'plain')

	html = "<em>This mail is sent from arduino,<strong>Happy Coding</strong></em>"
	part2 = MIMEText(html, 'html')

	username = '<EMAIL_ADDRESS>'
	password = mail['apiKey']
	msg.attach(part1)
	msg.attach(part2)
	s = smtplib.SMTP('smtp.mandrillapp.com:587')
	s.login(username, password)
	s.sendmail(msg['From'], msg['To'], msg.as_string())
	s.quit()