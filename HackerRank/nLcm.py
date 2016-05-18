t=int(input())
while(t>0):
    i = 1
    n=int(input())
    for k in (range(1, n+1)): 
      if i % k > 0: 
        for j in range(1, n+1): 
          if (i*j) % k == 0: 
            i *= j 
            break 
            
    print(i)
    