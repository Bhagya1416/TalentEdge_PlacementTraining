n=int(input())
s=0
for x in range(1,n//2+1):  
    if n%x==0:
        s=s+x
if s==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# A Perfect Number is a positive integer that is equal to the sum of its proper divisors
# Usually divisors and factors are same that's why we use the factors logic to find the perfect number. 
# The only difference is that we have to sum the factors and check if it is equal to the number or not.