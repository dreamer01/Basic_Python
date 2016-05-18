string=input()
subString=input()
n,c=0,0
for i in range(0,len(string)-len(subString)+1):
    if string[i]== subString[0]:
        j=0
        while j< len(subString):
            if string[i+j]==subString[j]:
                c=0
                j=j+1
            else:
                c=1
                break
        if c==0:
            n=n+1

print(n)
            