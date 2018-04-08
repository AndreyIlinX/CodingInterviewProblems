def int_to_binary(num):
    return "{0:b}".format(num)


def solution(pos_int):
    if not (isinstance(pos_int, int)):
        print("The input value is not an integer")
        return 0

    if pos_int < 0:
        return 0
    num_bin = int_to_binary(pos_int)
    max_bin_gap_size = 0
    bin_gap_size = 0
    i = len(num_bin) - 1
    while (i > 0):
        if num_bin[i] == '1':
            while (num_bin[i - 1] == '0' and i > 0):
                bin_gap_size = bin_gap_size + 1
                i = i - 1
            if bin_gap_size > max_bin_gap_size:
                max_bin_gap_size = bin_gap_size
            bin_gap_size = 0
        if i > 0:
            i = i - 1
    return max_bin_gap_size


def main():
    print(solution(1249))


if __name__ == '__main__':
    main()
