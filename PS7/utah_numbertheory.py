import random
import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def exp(x, y, n):
    result = 1
    x = x % n
    while y > 0:
        if (y & 1) == 1:  # Efficient bitwise operation for checking odd numbers
            result = (result * x) % n
        y >>= 1  # Efficient bitwise right shift operation equivalent to dividing by 2
        x = (x * x) % n
    return result


def inverse(a, N):
    for i in range(1, N):
        if (a * i) % N == 1:
            return i
    return "none"


def isprime(p):
    if p == 2:
        return "yes"
    if p % 2 == 0:
        return "no"
    for _ in range(5):
        a = random.randint(2, p - 1)
        if exp(a, p - 1, p) != 1:
            return "no"
    return "yes"


def key(p, q):
    modulus = p * q
    # Corrected variable shadowing issue by using 'phi' instead of reusing 'p'
    phi = (p - 1) * (q - 1)
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    d = inverse(e, phi)
    return f"{modulus} {e} {d}"


def main():
    for line in sys.stdin:
        tokens = line.strip().split()
        if not tokens:
            continue

        if tokens[0] == "gcd":
            print(gcd(int(tokens[1]), int(tokens[2])))
        elif tokens[0] == "exp":
            print(exp(int(tokens[1]), int(tokens[2]), int(tokens[3])))
        elif tokens[0] == "inverse":
            print(inverse(int(tokens[1]), int(tokens[2])))
        elif tokens[0] == "isprime":
            print(isprime(int(tokens[1])))
        elif tokens[0] == "key":
            print(key(int(tokens[1]), int(tokens[2])))


if __name__ == "__main__":
    main()
