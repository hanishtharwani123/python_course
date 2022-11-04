def fac(n):
    fac = 0
    for i in range(1,n+1):
        fac = fac + i
    return fac

c = sum(5)
print(c)

# RECURSION
def natur(n):
    if n == 1:
        return 1
    return n + natur(n-1) 

c = natur(5)
print(c)
