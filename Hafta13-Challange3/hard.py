def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


n = 30
r = 4

result = combination(n, r)

print(int(result), "farklı şekilde 4 kişi seçilebilir:")
