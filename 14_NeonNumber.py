# Sum of digits of n^2 equals n eg:9 
# Explanation: 9*9=81, 8+1=9
def is_neon(n):
    square=n*n
    digit_sum=sum(int(d) for d in str(square))
    return digit_sum==n
num=int(input())
print("Output:","Yes" if is_neon(num) else "No")

