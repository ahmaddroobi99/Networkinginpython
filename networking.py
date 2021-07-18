import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

server =smtplib.SMTP('smtp.gmail.com',25)
server.echlo()
server.login('mail@mail.com','password123')


with open('password.txt') as f :
    password = f.read ()
    
    
    
server.login("ahmad.droobi1999@gmail.com",password)
msg =MIMEMultipart()
msg [ 'From']='Ahamd droobi'
msg['To']= 'adroobi@asaltech.com'
msg ['Subject']= "jst a test from my python "


with open ('messge.txt','r')as f :
    messege = f.read ()




msg.attach(MIMEText(messege,'pain'))


filename ='5215.PNG'

attachment = open (filename,'rb')
p = MIMEBase ('application','octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header()









    

