splitLen = 10 # размер пачек


list_of_file = [1, 2, 3]

for i in list_of_file:
    input = open(r'C:\Users\admin\Downloads\{0}.txt'.format(i), 'r')
    outputBase = 'copy_file_{0}_'.format(i) # названия новых файлов

    count = 0
    at = 0
    dest = None
    for line in input:
        if count % splitLen == 0:
            if dest: dest.close()
            dest = open(outputBase + str(at) + '.txt', 'w')
            at += 1
        dest.write(line)
        count += 1

    if dest: dest.close()