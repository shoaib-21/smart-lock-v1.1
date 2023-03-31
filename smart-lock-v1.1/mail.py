import yagmail

def send_mail(username):
    mailId = yagmail.SMTP('smartlocka39@gmail.com')
    to1 = 'noormohd0845@gmail.com'
    to2= 'shoaib733021@gmail.com'
    #to = 'shoaib.ahmed011521@gmail.com'
    sub = 'MALICIOUS ACTIVITY'
    body =f"malicious activity detected from {username}, trying to login without loging out...."
    mailId.send(to1,sub,body)
    mailId.send(to2,sub,body)
#send_mail('shoaib')