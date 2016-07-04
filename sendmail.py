import smtplib
from email.mime.text import MIMEText
msg = MIMEText(text)
fromad = "krishna.rohith.sai@gmail.com"#the sender's email address
msg['Subject'] = 'The contents of %s' % "Colors"
msg['From'] = fromad
msg['To'] = to

password = 'Rohith24sai31&@1996'
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(fromad,password)
s.sendmail(fromad, [to], msg.as_string())
s.quit()