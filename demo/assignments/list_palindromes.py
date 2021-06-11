# Palindrome program
nums = [121, 123, 454, 555, 235]

for n in nums:
    s = str(n)   # Convert int to str
    if s == s[::-1]:
        print(s)