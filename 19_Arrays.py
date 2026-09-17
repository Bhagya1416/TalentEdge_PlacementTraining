# 15-09-2026
# Basic concepts of arrays
# 1.two-two digits swapping
n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)-1,2):
    a[i],a[i+1]=a[i+1],a[i]
print(a)
#multiply with 2 for the above output array
b=[]
for i in a:
    b.append(i*2)
print(b)


# 2.Max array finding
a=list(map(int,input().split()))
m1=a[0]
for i in a:
    if i>m1:
        m1=i
print(m1)


# 3.Second maximum array
a=list(map(int,input().split()))
m1=a[0]
m2=a[0]
for i in a:
    if i>m1:
        m2=m1
        m1=i
    elif i>m2 and i!=m1:
        m2=i
print(m2)


# 4.Finding the count
def ocu(a,k):
    c=0
    for x in a:
        if x==k:
            c+=1
    return c
a=list(map(int,input().split()))
k=a[0]
print(ocu(a,k))
        

# 5.All elements count
def ocu(a):
    s=set(a)
    for x in s:
        print(x,a.count(x))
n=int(input())
a=list(map(int,input().split()))
ocu(a)


# 6.Reverse of a array 
a=list(map(int,input().split()))
print(*a[::-1])

# Another logic
a=list(map(int,input().split()))
a.reverse()
print(*a)

