from primes import PRIMES


def main(n):
    factors = []

    prime_index = 0
    while True:
        prime_n = PRIMES[prime_index]
        # print(f"using prime {prime_n}")
        if n % prime_n == 0:
            factors.append(prime_n)
            print(f"\tYep {prime_n} goes in")
            n = n / prime_n
            print(f"New n: {n}")
            if n == 1:
                break
            prime_index -= 1
        prime_index += 1
    return factors


if __name__ == '__main__':
    print(main(600851475143))
