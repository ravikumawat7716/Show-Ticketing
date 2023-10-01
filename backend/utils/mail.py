from instances.app import app
from instances.mail import mail
from flask_mail import Message
import os

def send_mail(receiver_email , subject , body, attachment=None,mime_type = "application/pdf" ):
    try:
        msg = Message(recipients=[receiver_email],body=body,subject=subject)
        if attachment :
            with app.open_resource(attachment) as file:
                if mime_type == "application/pdf" :
                    msg.attach("report.pdf",mime_type , file.read())
                elif mime_type == "application/x-zip" :
                    msg.attach("exportedfile.zip",mime_type , file.read())
                elif mime_type == "text/csv":  
                    msg.attach("data.csv", mime_type, file.read())

        mail.send(msg)
    except Exception as e:
        print(e)
