def sieve(n):
    p = [False, False] + [True]*(n-2)
    for i in range(2,n+1):
        for j in range(i,n+1):
            if i*j < n:
                p[i*j]=False
    
    for i in range(2,n):
        if p[i]:
            print(i)

    print(p)
  
