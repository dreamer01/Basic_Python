X=int(input())
Y=int(input())
Z=int(input())
n=int(input())
a=[[x,y,z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x+y+z!=n]
print(a)