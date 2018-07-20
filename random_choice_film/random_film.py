import random

file_path = "C:\\Users\\admin\\Downloads\\films.txt"
new_file = "C:\\Users\\admin\\Downloads\\download.txt"


with open(file_path, 'r') as my_films, open(new_file, 'w') as new:
    film_list = my_films.read().split('\n')
    print('List contains ' + str(len(film_list)) + ' films.')
    quantity = int(input("How many films will you watch? "))
    choice = random.sample(film_list, quantity)
    result = '\n'.join(choice)
    print(result)
    new.writelines(result)
    #
    update_list = [x for x in film_list if x not in choice]
    new_film_list = ', '.join(update_list)

