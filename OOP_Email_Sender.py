
import smtplib
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.text import MIMEText
class Mail ():


 def __init__(self ,server):
     self.server =server

 def sendMail (self ,from_email ,password,to_email ,subject ,message ):
    msg = MIMENonMultipart()
    msg ['From']=from_email
    msg['To']=to_email
    msg['subject']=subject

    msg.attach(MIMEText (message,'plain'))
    try :
        server = smtplib.SMTP_SSL(self.server,465)
        server.ehlo()
        server.login(from_email,password,)
        server.sendmail(from_email,to_email,msg.as_string())
        server.close()
        return True
    except Exception as e:
        print('Something WEnt Wrong '+str(e))
        return False



senderObj = Mail('smtp.gmail.com')
senderObj.sendmail('layla.hamdan1999@gmail.com','***********','ahmad.droobi1999@gmail.com','Subject is sending u my Cv or stuff like that ','messahge-lksdvnksadnvglk;znfksdbnvsmdfmv;lkzd fb/m ;,s dv,l')
senderObj2 = Mail('smtp.gmail.com')
senderObj2.sendmail('layla.hamdan1999@gmail.com','***********','ahmad.droobi1999@gmail.com','Subject is sending u my Cv or stuff like that ','messahge-lksdvnksadnvglk;znfksdbnvsmdfmv;lkzd fb/m ;,s dv,l')


