import smtplib, ssl
import math
import random

def generateOTP() :
	digits = "0123456789"
	OTP = ""
	for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]
	
	return OTP

def send_otp(otp):
	port = 465
	smtp_server = "smtp.gmail.com"
	sender_email = "albertsosmarteinstein@gmail.com"  
	receiver_email = "dummysosmartuser@gmail.com"
	password = "WTGoVzMhGnh%R^^@budk7^2aDc9b#3Nv$XGkAPbsoLH"
		
	message = f"""\
        Subject: Hi there.
        \nYour OTP is {otp}, don't share it with anyone.
        This message is sent from Python."""

	context = ssl.create_default_context()

	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)

otp = generateOTP()	
send_otp(otp)