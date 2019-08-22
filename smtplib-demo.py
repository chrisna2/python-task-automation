import smtplib


smtp = smtplib.SMTP(host='smtp.naver.com', port=465)

smtp.sendmail('skgusrl2@naver.com', 'marksman703@gmail.com')

