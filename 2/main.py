# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file),
# которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
list = []
with open('article.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()
    max_length = len(max(words, key=len))
    for word in words:
        if len(word) == max_length:
            list.append(word)
print(list)