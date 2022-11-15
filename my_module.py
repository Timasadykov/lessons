from random import randint, shuffle,  random, choice

# a = 4
# print(n)
# print(n + a)

# num2

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

# print(choice(names))

# a = ('aibek , bolotbek, atai, bolotbek')
 





# num 3
# os.system('/home/admin1/lessons')




# num2.1


# import sys
# for i in range(2):
#     input ( ' введите значения:')
# print (sys.version)
# print ( sys.getsizeof(i))




# num31
# from string import ascii_letters, digits
# from time import sleep

# while True:
#     password = ''
#     while len(password) < 8:
#         choice1 = choice(ascii_letters)
#         password += choice1

#     print(password)
#     sleep(3)




print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")