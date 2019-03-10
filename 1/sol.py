import math


def main_slow(max_number):
    summ = 0
    for i in range(0, max_number):
        if i % 3 == 0:
            summ += i
        elif i % 5 == 0:
            summ += i
    print(summ)


def sumN(n):
    # returns sum of the first n numbers
    return n * (n + 1) / 2


def main(max_number):
    num_fives = math.floor(max_number / 5)
    sum_fives = sumN(num_fives) * 5

    num_threes = math.floor(max_number / 3)
    sum_threes = sumN(num_threes) * 3

    num_fifteens = math.floor(max_number / 15)
    sum_fifteens = sumN(num_fifteens) * 15

    sum_overall = sum_fives + sum_threes - sum_fifteens
    print(int(sum_overall))


if __name__ == '__main__':
    main(999)
