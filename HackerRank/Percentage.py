from pip._vendor.distlib.compat import raw_input
n=int(input());
i=0;
name=['a']*n
marks=[1]*n
while i<n:
    name[i],a,b,c=map(str,raw_input().split())
    a=int(a)
    b=int(b)
    c=int(c)
    marks[i]=a+b+c
    i=i+1
s=raw_input()
i=0;
while i<n:
    if name[i]==s:
        print("%.2f" % round(a,2))
    i=i+1
