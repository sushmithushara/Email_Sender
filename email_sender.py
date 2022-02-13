import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html =Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Sushmi Thushara'
email['to'] = 'sushmithushara@gmail.com'
email['subject'] = 'Excercise for ZTM - Python Class'
email.set_content(html.substitute({'name' : 'Sushmi Thushara'}),'html')

with smtplib.SMTP(host = 'smtp.yahoo.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('sushmithushara@yahoo.com','**********')
	smtp.send_message(email)
	print("All good now")
