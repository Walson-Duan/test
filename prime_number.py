from math import sqrt, floor


def is_prime(n):
    if n <= 1:
        return False
    elif n >= 4:
        if n % 2 == 0 or n % 3 == 0:
            return False
        else:
            ns = floor(sqrt(n))
            for x in range(5, ns + 1, 6):
                if n % x == 0 or n % (x+2) == 0:
                    return False

    return True


for m in range(1, 65538):
    if is_prime(m):
        print(m)
