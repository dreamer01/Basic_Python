n=int(input())
i=0
l=list()
while i<n:
    x=input()
    name=x.split() 
    if name[0]=='insert':
        a=int(name[1])
        b=int(name[2])
        l.insert(a,b)
    elif name[0]=='append':
        a=int(name[1])
        l.append(a)
    elif name[0]=='extend':
        a=int(name[1])
        l.extend(a)
    elif name[0]=='remove':
        a=int(name[1])
        l.remove(a)
    elif name[0]=='sort':
        l.sort()
    elif name[0]=='pop':
        l.pop()
    elif name[0]=='reverse':
        l.reverse()
    elif name[0]=='print':
        print(l)
    i=i+1