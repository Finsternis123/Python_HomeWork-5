#Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
a = int(input('Enter number а: '))
b = int(input('Enter number b: '))
result = 0
def sum(result):
    if a <= 0 and b <= 0:
        return 0
    else:
        return a + b
print (sum(result))