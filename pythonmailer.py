import smtplib


fromaddr = 'xxxx'
toaddr = 'xxxxx'
user = 'xxxxxx'
pas = 'xxxxxx'

def sendmail():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(user, pas)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()


msg = raw_input('Enter  a message to send please.... ')

sendmail()
