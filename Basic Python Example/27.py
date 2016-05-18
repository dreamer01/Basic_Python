a=int(input("Enter  Number A : ")) 
b=int(input("Enter  Number B : ")) 

def lcm(a,b):
    for i in range(1,b+1):
        for j in range(1,a+1):
            if(a*i==b*j):
                return a*i
        
      
l=0
l=lcm(a,b)
print("The LCM of {} and {} is : ".format(a,b),l)