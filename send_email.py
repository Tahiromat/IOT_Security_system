import smtplib
from email.message import EmailMessage
# hcmpugotdcymfzqf   # third party apps password for mail server


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'matahir33@gmail.com'
    msg['from'] = user
    password = 'hcmpugotdcymfzqf'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


# if __name__ == '__main__':
#   email_alert('Security problem', 'Some movements recognized', 'tahirmat@protonmail.com')