n=int(input("Enter A Number : ")) 

a=[]
i=0
while n!=0:
    a.append(int(n%2))
    i=i+1
    n=int(n/2)

a.reverse()   
print("The Binary : ",a)
