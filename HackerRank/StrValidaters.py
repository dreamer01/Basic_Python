st=input()
i=''
#print(type(i))
#print(type(str))
for i in st:
    if i.isalnum()==True:
        print(i.isalnum())
        break;
    else:
        if i==st[-1]:
            print(False)

for i in st:
    if i.isalpha()==True:
        print(i.isalpha())
        break;
    else:
        if i==st[-1]:
            print(False)
            
for i in st:
    if i.isdigit()==True:
        print(i.isdigit())
        break;
    else:
        if i==st[-1]:
            print(False)
            
for i in st:
    if i.islower()==True:
        print(i.islower())
        break;
    else:
        if i==st[-1]:
            print(False)
            
for i in st:
    if i.isupper()==True:
        print(i.isupper())
        break;
    else:
        if i==st[-1]:
            print(False)
