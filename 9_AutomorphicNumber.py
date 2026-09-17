# Square of a number ends with a number itself eg:5^2=25

# This will work only for single digit code
n=int(input())
r=n**2
digit=r%10
if digit==n:
    print("Automorphic")
else:
    print("No")


# The below code work for any input
n = int(input())
r = n ** 2
temp = n
digits = 0
while temp > 0:
    digits += 1
    temp //= 10
last_digits = r % (10 ** digits)
if last_digits == n:
    print("Automorphic")
else:
    print("No")


# The below code write using function this will work for any input
def is_automorphic(n):
    return str(n*n).endswith(str(n))
num=int(input())
if is_automorphic(num):
    print("Automorphic")
else:
    print("No")
    
