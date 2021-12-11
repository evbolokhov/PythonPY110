# task_1
# def bin_to_dec(bin_list):
#     bin_str = "".join(str(x) for x in bin_list)
#     return int(bin_str, 2)
#
# print(bin_to_dec([0, 1, 1, 0, 1]))
#
# # task_2
#
# str_ = 'hello'
# lst = []
#
# for index, znach in enumerate(str_):
#     if znach == ' ':
#         continue
#     if znach.isalpha():
#         a = str_[:index]
#         b = str_[index + 1:]
#         lst.append(''.join((a, znach.upper(), b)))
#         print(lst)

# task_4
# rus_alphabet = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])
# print(rus_alphabet)
# def get_rus_alphabet_with_weight():
# weight_dict = {}
# for weight, elem in enumerate(rus_alphabet, start=1):
#     weight_dict.update({elem: weight})
#
# print(weight_dict)
#
# word_list = 'мама мыла раму'.split(" ")

# task 5


import requests

# тело запроса для создания нового пользователя
user = {"name": "Fred”, "age": 25,"mail":"fr @ mal.com", "password": "134513"}
        r = requests.post("http://localhost/users/", data=user)
# напечатать код запроса
print(r.status_code)
# GET запрос на получение пользователя по id
url = "http://localhost/users/” + str(r.json()['id'])
r = requests.get("http://localhost/users/”, data=user)
print(r.text)







