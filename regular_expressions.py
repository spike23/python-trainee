import re
import os

file_path = 'C:\\Users\\admin\\Downloads\\'
file_name = 'dataJul-9-2018.csv'
new_name = 'results.txt'
new_file = os.path.join(file_path, new_name)
my_file = os.path.join(file_path, file_name)

my_list = []
with open(my_file, 'r') as f:
    for row in f:
        my_list.append(row)

my_string = ' '.join(my_list)

text_look_for = r'[\w._-]+@[\w._-]+\.[\w.]+'
result = re.findall(text_look_for, my_string)

with open(new_file, 'w') as nf:
    nf.write('\n'.join(result))
    # nf.writelines(["{0}\n".format(item)  for item in result])  ---- второй способ записи
'''
\d - любые цифры [0-9]
\D - любой символ, кроме цирфы
\w - любой алфавитный символ [a-z]
\W - любой символ, кроме алфавитного
\s - поиск пробела
\S - любой символ, кроме пробела
примеры:
\d\d\d или \d{3} - три подряд стоящие цифры
[A-Z]\w+ - слова начинающиеся с заглавных букв (+ это любое количестов символов после указаных перед +)
@\w+\.\w+ - поиск доменов электронных почт (@gmail.com)
[\w._-]+@[\w._-]+\.[\w.]+' - поиск электронных почт (любых)
'[\w._-]+@(?!nisl\.net)[\w._-]+\.[\w.]+' - поиск электронных почт (кроме домена @nisl.net)
'''