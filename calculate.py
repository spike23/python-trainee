a = float(input())
b = float(input())
c = input('Выберите операцию (+), (-), (*), (/), (mod), (div), (pow): ')
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/' and b != 0:
    print(a / b)
elif c == 'mod' and b != 0:
    print(a % b)
elif c == 'pow':
    print(a ** b)
elif c == 'div' and b != 0:
    print(a // b)
else:
    print('Деление на 0!')

'''Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и
 операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и
 выводит результат на экран. Поддерживаемые операции: +, -, /, *, mod, pow, div, где:
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.
Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
Обратите внимание, что на вход программе приходят вещественные числа.

'''