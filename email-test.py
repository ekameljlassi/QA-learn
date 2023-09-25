import smtplib, ssl
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "kamel.jlassi@gomycode.co"
receiver_email = "kameljs2@gmail.com"
password = ""
message = """\
Subject: Hi there
Im sending an email through python code."""
print(sender_email)
print(password)
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo() 
    server.starttls(context=context)
    server.ehlo() 
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message) 