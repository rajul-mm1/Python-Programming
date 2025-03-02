import math

def lcm(a,b):
    gcd = math.gcd(a,b)
    return a*b//gcd

p,n = map(int,input().split())

print(lcm(p,n))