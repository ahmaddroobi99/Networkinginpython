import smtplib
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.text import MIMEText

def sendMail (from_email ,password,to_email ,subject ,message ):
    msg = MIMENonMultipart()
    msg ['From']=from_email
    msg['To']=to_email
    msg['subject']=subject

    msg.attach(MIMEText (message,'plain'))
    try :
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.login(from_email,password,)
        server.sendmail(from_email,to_email,msg.as_string())
        server.close()
        return True
    except Exception as e:
        print('Something WEnt Wrong '+str(e))
        return False

