import sys
import math

def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

#print exp x^y mod n
def exp(x, y, z):
    res = 1
    while(y > 0):
        if y%2 == 0:
            x = (x*x)%z
            y /= 2
        else:
            res = (x*res)%z
            y -= 1
    return res

def ee(a,b):
    if b == 0:
        return [1, 0, a]
    else:
        l = ee(b, a%b)
        return [l[1], l[0] - (a/b)*l[1], l[2]]

# print modular multipicative inverse or "none"
def inverse(x, y):
    l = ee(x, y)
    if l[2] == 1:
        return l[0]%y
    else:
        "none"

def isprime(x):
    if(fermat(x, 2) and fermat(x, 3) and fermat(x, 5)):
        return "yes"
    else:
        return "no"

def fermat(x, a):
    if exp(a, x-1, x) == 1:
        return True
    else:
        return False

# Print mod, public exp, and private exp
def key(x, y):
    m = x * y
    phi = (x-1)*(y-1)

    pub = 2
    while pub < phi:
        if gcd(phi, pub) == 1:
            priv = inverse(pub, phi)
            if priv != None:
                print m, pub, priv
                return
        pub += 1


for line in sys.stdin:
    data = line.split()
    if data[0] == "gcd":
        print gcd(int(data[1]), int(data[2]))
    if data[0] == "exp":
        print exp(int(data[1]), int(data[2]), int(data[3]))
    if data[0] == "inverse":
        print inverse(int(data[1]), int(data[2]))
    if data[0] == "isprime":
        print isprime(int(data[1]))
    if data[0] == "key":
        key(int(data[1]), int(data[2]))
