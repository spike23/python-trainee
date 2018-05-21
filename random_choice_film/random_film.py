import random

my_films = open("C:\\Users\\admin\\Downloads\\films.txt").read().split('\n')
filmlist = []
a = int(input("How many films will you watch? "))
for i in my_films:
    filmlist.append(i)
choice = random.sample(filmlist, a)
print(choice)
