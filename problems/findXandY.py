from math import gcd
def findXandY(A,B,N):
    g = gcd(A,B)
    if N%g!=0:
        return -1
    for y in range(N):
        if (N-B*y)//A:
            x = (N-B*y)//A
            return x,y
    return -1
print(findXandY(2,3,7))