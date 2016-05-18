a=int(input("Enter  Number A : ")) 
b=int(input("Enter  Number B : ")) 

def hcf(x, y):
    while(y):
        x, y = y, x % y
    return x
h=hcf(a,b)
print("The HCF of {} and {} is : ".format(a,b),h)
