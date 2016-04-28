X = int(input())  # кол-во минут для сна
H = int(input())
M = int(input())
print((X + M) // 60 + H)  # часы пробуждения
print((X + M) % 60)  # минуты пробуждения

""" Катя узнала, что ей для сна надо XX минут. В отличие от Коли, Катя ложится спать после полуночи в HH часов и MM
минут Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через XX минут после
того, как она ляжет спать. На стандартный ввод, каждое в своей строке, подаются значения XX, HH и MM.
Гарантируется, что Катя должна проснуться в тот же день, что и заснуть.
Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты."""