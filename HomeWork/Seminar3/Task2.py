#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import string

with open ('text.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
for char in string.punctuation:
    data = data.lower().replace(char, ' ')
count_dict={}

for word in data.split():
    count_dict[word] = count_dict.get(word, 0) + 1
count_dict = tuple (sorted(count_dict.items(), key=lambda item: item [1]))
for index, word in enumerate(count_dict[-1:-10:-1], 1):
    print(f' {index}. {word[0]:>10} {word [1]} раз')