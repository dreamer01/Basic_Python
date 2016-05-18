from math import sqrt
t=int(input())
while t>=0:
    n=input()
    l=n.split()
    n1=int(l[0])
    n2=int(l[1])
    c=0;
    for i in range(n1,n2+1):
        for j in range(1,i//2):
            if j==sqrt(i):  #checking for integer from 1 to num for its sqrt
                c=c+1;
    print(c)
    t=t-1