def pattern(n):
    x = 0
    for i in range(0, n):
        x += 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")

pattern(7)


#pascal's triangle
def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(function(i,j)," ", end="")
        print()

def funtion(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0,k):
        res = res * (n-i)
        res = res//(i+1)
    return res

pattern(7)