# 1+X+X^2+X^3+.......+X^N
x=float(input())
n=int(input())
total=0
for i in range(0,n+1):
    total+=x**i
print(total)


# 1-x+x^2-x^3+..........x^n
x=float(input())
n=int(input())
total=0
for i in range(0,n+1):
    if i%2==0:
        total+=x**i
    else:
        total-=x**i
print(total)


# To print like this 1 + 2^1 + 2^2 + 2^3 + 2^4 + 2^5
x=int(input())
n=int(input())
for i in range(0,n+1):
    if i==0:
        print(1,end=" ")
    else:
        print(f"+ {x}^{i}",end=" ")