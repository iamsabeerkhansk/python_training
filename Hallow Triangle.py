n = int(input())
for i in range(n):
    for j in range(i+1):
        if i==j or i==n-1 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()