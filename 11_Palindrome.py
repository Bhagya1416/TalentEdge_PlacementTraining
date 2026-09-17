def is_palindrome(n):
    return str(n)[::-1]
num=int(input())
if is_palindrome(num)==str(num):
    print("Palindrome")
else:
    print("No")
