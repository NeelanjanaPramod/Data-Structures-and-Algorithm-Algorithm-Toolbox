# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1
    n = n%60
    if (n == 0):
        return 0
    for _ in range(n - 1):
        previous, current = current%10, (previous + current)%10
        sum += (current%10)

    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    m, n = map(int, input().split())

    print((fibonacci_sum_naive(n) - fibonacci_sum_naive(m - 1) + 10) % 10)
