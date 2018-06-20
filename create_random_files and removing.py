import random
import os

my_folder = 'C:/Users/admin/Downloads/temp2/'


def remove_files():
    for files in os.listdir(my_folder):
        file_path = os.path.join(my_folder, files)
        os.unlink(file_path)


def create_files(min_num, max_num):
    qnt_files = random.randint(min_num, max_num)
    list_of_files = [random.randrange(1, 10) for i in range(qnt_files)]
    count = 0
    for my_file in list_of_files:
        with open(os.path.join(my_folder, '{0}.txt'.format(my_file)), 'w') as f:
            pass
        f.close()
        count += 1
    if count % 10 == 1:
        print(str(count) + " файл")
    elif count % 10 == 2 or count % 10 == 3 or count % 10 == 4:
        print(str(count) + " файла")
    else:
        print(str(count) + " файлов")


print('Хотите создать n количество экземпляров файлов?')
answer = str(input('Да - нажмите Y, Нет - нажмите N: '))

if answer == 'Y' or answer == 'y':
    min_num = int(input('Введите минимальное количество создаваемых файлов: '))
    max_num = int(input('Введите максимальное количество создаваемых файлов: '))
    create_files(min_num, max_num)
else:
    print('Программа завершена')
    exit()


print('Очистить содержимое директории? ')
answer_2 = str(input('Да - нажмите Y, Нет - нажмите N: '))

if answer_2 == 'Y' or answer_2 == 'y':
    remove_files()
    print('Очистка успешно завершена')
else:
    print('Программа завершена')
    exit()
