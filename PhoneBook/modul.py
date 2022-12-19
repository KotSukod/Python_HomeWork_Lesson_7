import phone_base
import input
import view


def great_contact ():

    name = input.input_name()
    surname = input.input_surname()
    tel = input.input_number()
    proverka = phone_base.search_for_duplicates(tel)
    if proverka == 1:
        print('Такой номер телеофна уже существует!!!')
    else:
        phone_base.great(name, surname,tel)
        print("Запись создана")

def search():
    tel = input.input_number()
    number = phone_base.search_number(tel)
    if number == None:
        print("Номер не найден")
    else:
        print("{}-{}-{}".format(number[0],number[1],number[2]))

def change_data():
    tel = input.input_number()
    number,index = phone_base.search_number(tel)
    print("Какие данные будем редактировать:")
    print("1 - Имя")
    print("2 - фамилия")
    print("3 - Телефон")
    value = view.get_value()
    if value == 1:
        name = input.input_name()
        number[0] = name
    if value == 2:
        surname = input.input_surname()
        number[1] = surname
    if value == 3:
        tel = input.input_number()
        number[2] = tel
    phone_base.base_save(number[0],number[1],number[2],index)

def delet():
    tel = input.input_number()
    number,index = phone_base.search_number(tel)
    phone_base.base_delet(index)
    print("Запись удаленна")