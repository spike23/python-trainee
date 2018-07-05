import random
# создаем список случайных чисел
search_list = [random.randrange(1, 100) for x in range(1, 16)]
# сортируем массив
search_list.sort()
# выбираем число для поиска случайным образом
num = random.choice(search_list)


def binary_search(search_list, num, start, stop):
    if start > stop:
        print('Item ' + str(num) + ' not found')
        return False
    else:
        mid_element = (start + stop) // 2
        if num == search_list[mid_element]:
            print('Item ' + str(num) + ' found at index ' + str(mid_element))
            return mid_element
        elif num < search_list[mid_element]:
            return binary_search(search_list, num, start, mid_element - 1)
        else:
            return binary_search(search_list, num, mid_element + 1, stop)


if __name__ == '__main__':
    print(search_list)
    binary_search(search_list, num, 0, len(search_list))
