# task_1
def bin_to_dec(bin_list):
    bin_str = "".join(str(x) for x in bin_list)
    return int(bin_str, 2)


if __name__ == "__main__":
    print(bin_to_dec([0, 1, 1, 0, 1]))
