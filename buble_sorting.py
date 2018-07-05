import random


# создаем список случайных чисел
search_list = [random.randrange(1, 100) for x in range(1, 8)]


def buble_sorting(search_list):
    last_item = len(search_list) - 1
    for x in range(0, last_item):
        for i in range(0, last_item-x):
            print(search_list)
            if search_list[i] > search_list[i+1]:
                search_list[i], search_list[i+1] = search_list[i+1], search_list[i]
    return search_list


if __name__ == '__main__':
    print("Old list: ", search_list)
    new_list = buble_sorting(search_list).copy()
    print("New list: ", new_list)