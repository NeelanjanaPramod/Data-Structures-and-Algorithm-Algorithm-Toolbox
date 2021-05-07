# Uses python3
def gcd(a, b):
    number1 = a
    number2 = b
    if (a == 0 ):
        return b
    if (b == 0 ):
        return a
    if a>= b:
        current_gcd=gcd(b,a%b)
    else:
        current_gcd=gcd(a,b%a)
    return current_gcd


a, b = map(int, input().split())
print(a*b//gcd(a, b))




