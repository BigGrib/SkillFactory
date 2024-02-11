# def say_hello(): print('Hello')
# def say_bye(): print('bye')

#локальные функции
# def print_mess():
#     def say_hello(): print("hello")
#     def say_bye(): print ("bye")
#     say_bye()
#     say_hello()
# print_mess()
# парпметры функции
#def (имя функции)([параметры]):
# def say_hello(name,age):
#     print(f' hello, {name}, {age}')
#
# say_hello('grib',34)
# say_hello('bob',23)
# say_hello(input(),input())

# # значение по умолчанию
#
# def say_hello(age,name='Bob'):  обязательный параметр идет 1
#     print(f"hello {name}, {age}")
#
# say_hello(32)

# * - устанавливает именнованные параметры, передача значений только по имени, справа от *
# def print_mess(name,*, age, company):
#     print(f'[{name},{age}, {company}]')
# print_mess('Bob',age = 32,company='compa')


# def print_mess(*,name, age, company):
#     print(f'[{name},{age}, {company}]')
# print_mess(name='Bob',age = 32,company='compa')

# / позициооные параметры, как *, но параметры получают тоько по позиции

# неопределенное кол-во параметров
# def sum(*numbers):
#     res=0
#     for i in numbers:
#         res +=i
#     return res
# print(sum(1,1,1,1,1,1,1,1))

# функция как тип
# def say(): print(input())
# mas = say
# mas()