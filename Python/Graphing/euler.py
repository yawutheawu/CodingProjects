import decimal


def factorial(n):
    factorials = [1]
    for i in range(1, n + 1):
        factorials.append(factorials[i - 1] * i)
    return factorials


def compute_e(n):
    decimal.getcontext().prec = n + 1
    e = 2
    factorials = factorial(2 * n + 1)
    for i in range(1, n + 1):
        counter = 2 * i + 2
        denominator = factorials[2 * i + 1]
        e += decimal.Decimal(counter / denominator)
    return e


n = int(input("Please type number: "))

print(str(compute_e(n))[:n + 1])
