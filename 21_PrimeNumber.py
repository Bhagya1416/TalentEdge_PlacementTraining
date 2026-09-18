# 17-09-2026
n=int(input())
if n>0:
    for i in range(2,n//2+1):
        if n%i==0:
            print("No")
            break
    else:
        print("Prime")
else:
    print("No")


# Prime numbers up to the given number and the count
def is_prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())
count=0
for x in range(2,n+1):
    if is_prime(x):
        print(x,end=" ")
        count+=1
print()
print("Count=",count)


# Logic question
n=int(input())
c1=c2=c3=0
for i in range(n+1):
    if i%3==0 and i%5==0:
        c1+=1
    elif i%3==0:
        c2+=1
    elif i%5==0:
        c3+=1
print(c1, c2, c3)
    

    

