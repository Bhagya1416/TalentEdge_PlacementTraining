n=int(input())
for x in range(1,n//2+1):  
    #for factors of any number we have to check till n//2 only because no number can be a factor of n if it is greater than n//2
    #Even if we take (1,n) that will print the factors but it is the worst case
    if n%x==0:
        print(x)
