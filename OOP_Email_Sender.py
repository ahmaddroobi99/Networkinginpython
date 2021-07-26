
import smtplib
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.text import MIMEText
class Mail ():


 def __init__(self ,server,from_email, password):
     self.server =server
     self.from_email = from_email
     self.password =password



 def sendMail (self ,to_email ,subject ,message ):
    msg = MIMENonMultipart()
    msg ['From']=self.from_email
    msg['To']=to_email
    msg['subject']=subject

    msg.attach(MIMEText (message,'plain'))
    try :
        server = smtplib.SMTP_SSL(self.server,465)
        server.ehlo()
        server.login(self.from_email,self.password,)
        server.sendmail(self.from_email,to_email,msg.as_string())
        server.close()
        return True
    except Exception as e:
        print('Something WEnt Wrong '+str(e))
        return False



senderObj = Mail('smtp.gmail.com','layla.hamdan1999@gmail.com','***********')
senderObj.sendmail('ahmad.droobi1999@gmail.com','Subject is sending u my Cv or stuff like that ','messahge-lksdvnksadnvglk;znfksdbnvsmdfmv;lkzd fb/m ;,s dv,l')
senderObj2 = Mail('smtp.gmail.com','layla.hamdan1999@gmail.com','***********')
senderObj2.sendmail('ahmad.droobi1999@gmail.com','Subject is sending u my Cv or stuff like that ','messahge-lksdvnksadnvglk;znfksdbnvsmdfmv;lkzd fb/m ;,s dv,l')


