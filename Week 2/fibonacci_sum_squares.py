# Uses python3
def fibonacciModulo(n):
    # Getting the period

    # Taking mod of N with
    # period length
    n = n % 60

    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n - 1):
        previous, current \
            = current % 10, (previous + current) % 10

    return (current)


# Driver Code
if __name__ == '__main__':
    n = int(input())
    print(fibonacciModulo(n) * fibonacciModulo(n + 1)%10)
