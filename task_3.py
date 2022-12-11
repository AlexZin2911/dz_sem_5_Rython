# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Восстановить
# Ввёл: stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"




# Сделал как работа с файлами, так и чисто консоль, консоль закомментировал, чтобы задача была выполнена по дз.
# Сначала напишите сжимаемый текст в файле text_input.txt, затем получите результат в файле text_output.txt.
# Для набора и отображения в консоли раскомментируйте оставшиеся строки кода.

# with open('text_input.txt', 'w', encoding='UTF-8') as file:
#     file.write(input('Напишите текст необходимый для сжатия: '))
with open('text_input.txt', 'r') as file:
    my_txt = file.readline()
    txt_compr = my_txt.split()

# print(my_txt)

def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


txt_compr = file_encod(my_txt)

with open('text_output.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compr}')
# print(txt_compr)
