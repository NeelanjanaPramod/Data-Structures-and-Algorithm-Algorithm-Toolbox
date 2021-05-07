def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1
    n = n%60
    if (n == 0):
            return 0

    for _ in range(n-1):
        previous, current = current%10, (previous + current)%10
        sum += (current%10)

    return sum % 10

m, n = map(int, input().split())
if (m==0):
  print((fibonacci_sum_naive(n)))
elif ( m<=n):
  print((fibonacci_sum_naive(n)-fibonacci_sum_naive(m-1)+ 10)%10)