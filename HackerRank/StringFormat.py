n=int(input())
for i in range(1,n+1):
    print(i,end=" ")
    o=oct(i)
    print(o,end=" ")
    print(hex(i),end=" ")
    print(bin(i),end=" ")
    print()