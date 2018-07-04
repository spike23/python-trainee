

#  рекурсия
def recursion(num):
    if num == 0:
        return
    else:
        print("Hello World!")
        recursion(num -1)


# сумма от разложенного числа (0+1+2+3+4+5)
def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return num + sum_of_digits(num - 1)


# факториал (1*2*3*4*5)
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)


# фибоначчи (0,1,1,2,3,5,8,13,21,34,55,88...n)
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num -1) + fibonacci(num -2)


if __name__ == '__main__':
    recursion(10)
    print(sum_of_digits(5))
    print(factorial(5))
    print(fibonacci(7))
