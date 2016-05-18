# Enter your code here. Read input from STDIN. Print output to STDOUT
import hashlib
n=input()
a,b=map(str,raw_input().split())
a=int(a)
b=int(b)
t=(a,b)
print hash(t)
