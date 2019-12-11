import smtplib

sender = 'adresnadawcy@domena.com'
receivers = ['adresodbiorcy@domena.com']

message = """From: From Nadawca <adresnadawcy@domena.com>
To: To Odbiorca <adresodbiorcy@domena.com>
Subject: Tytul e-maila

Tresc e-maila
"""

try:
	mail = smtplib.SMTP('localhost')
	mail.sendmail(sender, receivers, message)
	print ("E-mail wyslany!")
except SMTPException:
	print ("Error: Nie udalo sie wyslac e-maila!")
