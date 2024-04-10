import imaplib
import email
user, password="usermailID","password"
user_1, password_1= "usermailID","password"
imap_url = 'imap.gmail.com'
imap_url_1 = 'imap.gmail.com'
my_mail = imaplib.IMAP4_SSL(imap_url)
my_mail_1 = imaplib.IMAP4_SSL(imap_url_1)
my_mail.login(user, password)
my_mail_1.login(user_1, password_1)

def nishanth():
    my_mail_1.select('Inbox')
    key = 'TO'
    value = "usermailID"
    _, data = my_mail_1.search(None, key, value)
    # print(data)
    mail_id_list = data[0].split()
    usr=[]
    sub=[]
    count = 1
    msgs = []

    for num in reversed(mail_id_list):
        if count < 6:
            typ, data = my_mail_1.fetch(num, '(RFC822)')
            msgs.append(data)
            count += 1
        else:
            continue
    for msg in reversed(msgs[::-1]):
        for response_part in msg:
            if type(response_part) is tuple:
                my_msg = email.message_from_bytes((response_part[1]))
                From = my_msg['from']
                From_1 = From.split("<")
                Msg = my_msg['subject']
                usr.append(From_1[0])
                sub.append(Msg)
    return usr,sub
def main():
    my_mail.select('Inbox')
    key = 'TO'
    value = "usermailID"
    _, data = my_mail.search(None, key, value)
    mail_id_list = data[0].split()
    usr=[]
    sub=[]
    count = 1
    msgs = []

    for num in reversed(mail_id_list):
        if count < 6:
            typ, data = my_mail.fetch(num, '(RFC822)')
            msgs.append(data)
            count += 1
        else:
            continue
    for msg in reversed(msgs[::-1]):
        for response_part in msg:
            if type(response_part) is tuple:
                my_msg = email.message_from_bytes((response_part[1]))
                From = my_msg['from']
                From_1 = From.split("<")
                Msg = my_msg['subject']
                usr.append(From_1[0])
                sub.append(Msg)
    return usr,sub


