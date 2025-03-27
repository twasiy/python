import smtplib as s
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login("","")
sub = input('Enter subjects.')
body = input('Enter body.')
mass = f'subject:{sub}\n\n{body}'
listmail = input('ENter email:')
ob.sendmail('tassokimamwasiy58@gamil.com',listmail,mass)
print('email sent')
ob.quit()


# print(f"{"wasiy"}\n\n{"Tanha"}")