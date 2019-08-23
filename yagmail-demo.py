import yagmail

yag = yagmail.SMTP(user='skgusrl2', password='', host='smtp.daum.net', port=465)

yag.send(to='skgusrl2@naver.com', subject='야그메일 보내기', contents='야그댜 야그다 다크다크다크...')