def enumerate_(list_: list) -> iter:
    list_index_ = []
    i = 0
    for _ in range(len(list_)):
        list_index_.append(i)
        i += 1
    return zip(list_index_, list_)


if __name__ == "__main__":
    input_list_ = [19, 5, 5, 6, 2, 11, 5, 32, 25, 1]

    print(list(enumerate_(input_list_)))
