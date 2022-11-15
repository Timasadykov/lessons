# fib1 = 1
# fib2 = 1
 
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
 
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
 
# print("Значение этого элемента:", fib2)



# NUM3
def fib(n):
    f1 = f2 = 1
    print (f1)
    print (f2)
    for i in range(2, n+1):
        f1, f2 = f2, f1 + f2
        print(f2)
    

fib(n=n)


# 1
# a = []
# def sau_hello():
#     new_name = input("введите имя ?")
#     for new_name in a:

#         sau_hello(a)
#     else:
#         a.append(new_name)
#         print("имя добавлено")
#         sau_hello(a)
        







