n=int(input())
x=input()
a=list(map(int,x.split()))
#a= list(map(int,y))
#print(a)
c=max(a)
i=0
l=len(a)
while i<l:
    if a[i]==c:
        a.remove(c)
        l=len(a)
    else:
        i=i+1

r=max(a)
print(r)