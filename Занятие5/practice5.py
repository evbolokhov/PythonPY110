
# task_1
# def bin_to_dec(bin_list):
#     bin_str = "".join(str(x) for x in bin_list)
#     return int(bin_str, 2)
#
#
# print(bin_to_dec([0, 1, 1, 0, 1]))
# print(bin_to_dec([1, 1, 1, 0, 0, 1, 1, 0, 1]))
# print(bin_to_dec([0, 1, 1, 0, 1, 1, 1, 1]))


# task_2
# def wave(my_str):
    # simple
    # for i in range(len(my_str)):
    #     up_char = my_str[i].upper()
    #     print(f"{my_str[:i]}{up_char}{my_str[i + 1:]}")

    # gen
    # for elem in (f"{my_str[:i]}{my_str[i].upper()}{my_str[i + 1:]}" for i in range(len(my_str))):
    #     yield elem

    # lc
    # for elem in [f"{my_str[:i]}{my_str[i].upper()}{my_str[i + 1:]}" for i in range(len(my_str))]:
    #     print(elem)

    # pass

# wave("aaaaaaaa")
# gen = wave("aaaaaaaa")
# for _ in range(20):
#     print(next(gen))


# task_4 Решение 1
def get_rus_alphabet_with_weight():
    """Функция возвращает русский алфавит с весами для каждой буквы"""
    alphabet_weight = {}
    rus_alphabet = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])
    for weight, char in enumerate(rus_alphabet, 1):
        alphabet_weight.update({char: weight})

    return alphabet_weight


def get_word_with_max_weight(input_string):
    """Функция возвращает самое 'весомое' слово"""
    word_weight_list = []
    alphabet_weight = get_rus_alphabet_with_weight()

    word_list = input_string.split(" ")

    for word in word_list:
        word_weight = 0
        for char in word:
            word_weight += alphabet_weight.get(char, 0)
        word_weight_list.append(word_weight)

    return word_list[word_weight_list.index(max(word_weight_list))]

print(get_word_with_max_weight("мама мыла раму"))

# task_4 Решение 2
# def _height_word(word):
#     alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     alphabet_height = {}
#     for height, letter in enumerate(alphabet):
#         alphabet_height[letter] = height
#     return sum(alphabet_height[letter] for letter in word)
#
#
# def task_4(_str='мама мыла раму'):
#     _str = _str.split()
#     print(max(_str, key=_height_word))


# task 5 Решение 1

# def wrong_side(word):
#     center = len(word) // 2
#     if len(word) % 2 == 0:
#         first_revers = "".join(reversed(word[0:center]))
#         second_revers = "".join(reversed(word[center:]))
#         print(first_revers+second_revers)
#
#     else:
#         first_revers = "".join(reversed(word[0:center]))
#         second_revers = "".join(reversed(word[center+1:]))
#         print(first_revers + word[center] + second_revers)
#
#
# wrong_side("mouse")
# wrong_side("abcd")

# task 5 Решение 2

# def task_5(word='example'):
#     center = len(word)//2
#
#     print(word[center:-center])
#     return word[center-1::-1] + word[center:-center] + word[-center:][::-1]
#
#
# print(task_5())





