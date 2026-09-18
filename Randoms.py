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