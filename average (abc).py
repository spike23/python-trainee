
a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
c = int(input('Введите целое число: '))
if a > b and a < c or a > c and a < b:
    print(a)
elif b > a and b < c or b > c and b < a:
    print(b)
else:
    print(c)

