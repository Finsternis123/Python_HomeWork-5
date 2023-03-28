#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
a = int(input('Enter number а: '))
b = int(input('Enter number b: '))
def deg(a, b):
    if b == 1:
        return a
    else:
        return a * deg(a, b - 1)
print (deg(a, b))