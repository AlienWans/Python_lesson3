'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''
'''
    name = input('enter name')
    surname = input('enter surname')
    year = int(input('enter year'))
    city = input('enter city')
    email = input('enter email')
    telephone = input('input telephone')
'''
def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Ivanov', name = 'Sergey', year = '1992', city = 'Moscow', email = 'kiwiz697@gmail.com', telephone = '8-916-089-58-54')) 
