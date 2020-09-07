#star pyramid
def pattern(n):
    k = 2 * n + 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")
pattern(10)



#inverse pyramid
def pattern(n):
    k = 2 * n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")
pattern(10)




#Right start pyramid
def pattern(n):
    for i in range(0,n):
        for j in range(0, i + 1):
            print("* ",end=" ")
        print("\r")
        for i in range(n, -1, -1):
            for j in range(0, i + 1):
                print("* ", end=" ")
            print("\r")
pattern(10)



#left start pyramid
def pattern(n):
    k = 2 * n - 2
    for i in range(0,n -1):
        for j in range(0,k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")
    k = k - 1
    for i in range(n - 1, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")
pattern(10)



#hourglass
def pattern(n):
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")
    k = 2 * n - 2
    for i in range(0, n + 1):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")
pattern(5)



#Right triangle pattern
def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")
pattern(10)



#left(right-angle) triangle
def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")
pattern(10)



#downward half pyramid
def pattern(n):
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ",end=" ")
        print("\r")
pattern(10)



#diamond pattern
def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ",end=" ")
        print("\r")
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")
pattern(10)



#diamond star pattern
for i in range(5):
    for j in range(5):
        if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
            print("*", end="")
        else:
            print(end=" ")
    print()