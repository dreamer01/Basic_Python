a=int(input("Enter  Number A : ")) 
b=int(input("Enter  Number B : ")) 

def factor(n):
    a=[]
    i=1
    for i in range(1,n+1):
        if(n%i==0):
            a.append(i)
                    
    return a

x=factor(a)
print(x)
y=factor(b)
print(y)