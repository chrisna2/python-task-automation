import smtplib
from email.mime.text import MIMEText
from email.header import Header


smtp = smtplib.SMTP(host='smtp.naver.com', port=587)

smtp.ehlo()
smtp.starttls()

smtp.login(user='skgusrl2', password="")

"""
smtp.sendmail(
    'skgusrl2@naver.com', 
    'skgusrl2@naver.com',
    'hello my name is gogogogogo')
"""

unpaid_list = ['skgusrl2@naver.com', 'marksman703@gmail.com', 'chrisna2@hanmail.net']

for customer in unpaid_list:

    msg = MIMEText('본문입니다. 돈내라고!!')
    msg['Subject'] = Header("돈내라 안내면 짜른다.", charset="UTF-8")
    msg['From'] = 'skgusrl2@naver.com'
    msg['To'] = customer

    smtp.send_message(msg)


smtp.quit()

print('main send..')