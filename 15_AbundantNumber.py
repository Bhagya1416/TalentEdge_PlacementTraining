# An abundant number is a number whose sum of its proper divisors is greater than the number itself.
# Proper divisors = factors of a number excluding the number itself.
def is_abundant(n):
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    return total
num=int(input())
print("Output:","Yes" if is_abundant(num)>num else "No")
