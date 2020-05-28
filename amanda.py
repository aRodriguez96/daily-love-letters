import datetime as dt
import time
import smtplib


def send_email(message):
    email_user = 'amandasnumberonefan2816@gmail.com'
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, 'iloveamanda2816')

    #EMAIL
    str = 'Hello baby, \nThis is today\'s quote that shows how much I love you and how much you mean to me.\n\n'+'\''+message+'\''+'\n\nI love you so much my sunshine <3' 
    server.sendmail(email_user,'aherr318@gmail.com', str)
    server.quit()
    print('done')

def send_email_at(send_time, mes):
    time.sleep(send_time.timestamp() - time.time())
    m = mes[5:]
    print(m)
    send_email(m)
    print('email sent')

def parse_file(f):
    myStack = []
    with open(f) as fp:
        for line in fp:
            if line != '\n':
                myStack.append(line.rstrip())
    return myStack


file = 'quotes.txt'
stack = parse_file(file)
'''
for x in range(len(stack)):
    print(stack.pop())
'''

first_email_time = dt.datetime(2020,5,27,20,48,0) # set your sending time in UTC
interval = dt.timedelta(minutes=1) # set the interval for sending the email

send_time = first_email_time
while True:
    send_email_at(send_time, stack.pop())
    send_time = send_time + interval






