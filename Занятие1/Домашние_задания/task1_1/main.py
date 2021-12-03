def enumer(list_: list):

    for number, char in list(zip(numbers, chars)):  # TODO поэлементно объединить numbers и chars
        print(f"{number}-{char}")
    print(list(enumerate(chars)))


if __name__ == "__main__":
    chars = ["a", "b", "c", "d", "e"]
    task(chars)