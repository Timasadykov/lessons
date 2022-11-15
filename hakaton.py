# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")




# NUM2


# a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
# a.append(13)
# print(a.count(13))
# print(len(a))
# a_13 = a.count(13)
# a_len = len(a)
# a_percent = a_13 * 100 / a_len
# print(a_percent)
# if a_percent == 70:
#     print('Совпадение,не думаю!')
# elif a_percent > 70:
#     print("Я так и знал")
# elif a_percent < 70:
#     print("Неужели")
# else:
#     print("")



# NUM3



# with open('database.txt', 'w') as f:
#     for i in range(3):
#         log = input('Введи логин: ')
#         pas = int(input('Введи пароль: '))
#         f.write(f'логин: {log} пароль: {pas}\n')


# with open('database.txt', 'r') as f:
#     text = f.read()
# print(text)


# print('Войди или зарегистрируйся')

# while True:
#     log = input('Введи логин: ')
#     if log in text:
#         print('Такой логин есть!')
#         pas = int(input('Введи пароль:'))
#         pas2 = int(input('Повтори пароль:'))
#         if pas == pas2:
#             with open('database.txt', 'a')as f:
#                 f.write(f'логин: {log} пароль: {pas}\n')
#                 print('Success')
#                 break
#         else:
#             print('Пароли не совпадают, регистрируйтесь заново')
#             while pas != pas2:
#                 pas = int(input('Введи пароль:'))
#                 pas2 = int(input('Повтори пароль:'))
#             else:
#                 with open('database.txt', 'a')as f:
#                     f.write(f'логин: {log} пароль: {pas}\n')
#                     print('Success')
#                     break

#     else:
#         print('Такого логина не существует, введи заново')




# num2



# dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# for key,value in dict1.items():
#     if value % 3 == 0:
#         print(f"{key}- hi")
#     elif value % 5 == 0:
#         print(f"{key} - bye")





# num3


# numbers= '4729461084'
# nums_sum = sum(float(x)) 
# for x in in str_num.split())



