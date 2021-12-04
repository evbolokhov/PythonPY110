import re


def task():
    word_list = [
        ",./ sdfsdf",
        "Ddfsdf",
        "@@##,sdfsdf",
        "123_sdfsdf",
        "123sdfsdf",
        ", s,dfsdf",
        "123, fewfew",
    ]

    # word_pattern = re.compile(r'\w+')  # TODO записать регулярное выражение для поиска слова любой длины
    word_pattern = re.compile(r'[a-zA-Z0-9]+')  # TODO записать регулярное выражение для поиска слова любой длины

    for word in word_list:
        a = re.search(r'\w+', word)
        # print(word_pattern.search(word).group())  # TODO вызвать от регулярного выражения методы search и group
        print(a)

if __name__ == "__main__":
    task()
