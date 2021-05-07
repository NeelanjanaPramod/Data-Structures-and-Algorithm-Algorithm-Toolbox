# Uses python3
import sys

def gcd(a, b):
    if (a == 0 ):
        return b
    if (b == 0 ):
        return a
    if a>= b:
        current_gcd=gcd(b,a%b)
    else:
        current_gcd=gcd(a,b%a)
    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))


