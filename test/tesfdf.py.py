import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "albertsosmarteinstein@gmail.com"  # Enter your address
receiver_email = "dummysosmartuser@gmail.com"  # Enter receiver address
password = """WTGoVzMhGnh%R^^@budk7^2aDc9b#3Nv$XGkAPbsoLH"""
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
