def fibonacci(n: int) -> int:
    """Return the `n`th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        print("nminus 1 = {0} - nminus2 = {1} -result = {2} ".format(n_minus1, n_minus2, result))
        n_minus2 = n_minus1
        n_minus1 = result

    return result

fibonacci(25)

print("****************************")

for i in range (36):
    print(i, fibonacci(i))


def multiply(x: float, y: float) -> float:
    return x * y

print(multiply(65, 256.8596325589986653))




