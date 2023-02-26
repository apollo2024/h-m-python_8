# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать 
# построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). 
# Протестируем функцию на файле «article.txt» со следующим содержимым:
find_out = int(input())
if find_out < 0:
    print(...)
else:
    with open('article.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines()[-find_out:]:
            print(line)
