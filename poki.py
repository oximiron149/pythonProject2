admin_name = "polina"
admin_password = "123"

name = input("введите имя")
password = input("введите пароль")

if name == admin_name:
    if password == admin_password:
        print("вы приняты в наше сообщество")
    else:
        print("имя-ок,пароль-нет")
else:
    print("вы не прошли наше испытание,вы будете уничтожены")