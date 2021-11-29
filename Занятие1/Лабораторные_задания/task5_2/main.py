from itertools import repeat

def task() -> list:
    temp_tuple = (0, 36.6, 100)
    iter_c_to_f = map(lambda temp: temp * (9 / 5) + 32, temp_tuple)
    # return list(map(round, iter_c_to_f, repeat(2))) # TODO  вернуть список температур по Фаренгейту
    return list(iter_c_to_f)

if __name__ == "__main__":
    print(task())
