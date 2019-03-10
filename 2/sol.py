def main(max_n):
    a = 1
    b = 2

    s = 2
    while True:
        c = a + b
        a = b
        b = c
        print(c)

        if c % 2 == 0:
            s += c

        if c >= max_n:
            break
    print(f"Sum: {s}")


if __name__ == '__main__':
    main(4000000)
