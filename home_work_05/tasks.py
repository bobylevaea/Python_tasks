# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# Пример:
#
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power_recursive(a, b):
    if b == 0:
        return 1
    else:
        return a * power_recursive(a, b - 1)

a = int(input("Введите число: "))
b = int(input("Введите степень: "))

print(f"{a} в степени {b} = {power_recursive(a, b)}")

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
# целых неотрицательных чисел. Из всех арифметических операций допускаются
# только +1 и -1. Также нельзя использовать циклы.
#
# Пример:
#
# 2 2
# 4

def sum_recursive(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum_recursive(a - 1, b + 1)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

print(f"Сумма чисел {a} и {b} = {sum_recursive(a, b)}")
