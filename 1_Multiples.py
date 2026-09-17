n=int(input())
c=0
for x in range(1,n):
    if x%3==0:
        print(x)
        c=c+1
print(c)

# This is the worst case to print the multiples of a number. 
# The simple logic we have to use to print the multiples 
# print(n//3)


