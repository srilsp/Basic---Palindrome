#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
n = 0
for a in range(9999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]: # end to beginning, counting down by 1
                n = a * b
print ("The Largest palindromic number made from the 3 digit number is:", n)
