username = 'AyseErdanisman'
password = '1234'
user = input('Username: ')
passw = input('Password: ')

isLoggedin = (username == user) and (password == passw)

if isLoggedin:
    print('Hoş Geldiniz')
else:
    print('Hatalı giriş')