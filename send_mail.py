# coding: utf8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

toaddr = ['<receivername@gmail.com>']
me = 'From:<sendername@gmail.com>'
you = 'To: ' + ', '.join(toaddr)

server = 'smtp.gmail.com' # Сервер отправитель
port = 587
user_name = 'sendername@gmail.com' # Адрес отправителя
user_passwd = 'password' # Пароль отправителя

# Формируем заголовок письма
msg = MIMEMultipart('mixed')
msg['Subject'] = 'theme'
msg['From'] = me
msg['To'] = ', '.join(toaddr[0]) # отправка адресату


# Формируем письмо
part1 = MIMEText('message text.', 'plain')
msg.attach(part1)

# Подключение
s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.ehlo()
# Авторизация
s.login(user_name, user_passwd)
# Отправка письма
s.sendmail(me, toaddr, msg.as_string())
s.quit()

