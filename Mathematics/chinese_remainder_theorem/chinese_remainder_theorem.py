# In this program we're going to use the ChineseRemainderTheorem for finding the smallest n
# such that n is r1 modulo n1 and r2 modulo n2.

# This function computes the Greatest Common Divisor of two integers a and b.

def gcd(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)

# This function finds d, x, and y such that d = gcd(a, b) and d = ax + by.

def extended_gcd(a, b):
    
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)
    return (d, x, y)

# Finally, the Chinese Remainder Theorem finds the smallest positive integer n such that
# n modulo n1 is r1, and n modulo n2 is r2.

def ChineseRemainderTheorem(n1, r1, n2, r2):
    (d, x, y) = extended_gcd(n1, n2)
    initial_n = r2*x*n1 + r1*y*n2
    k = (abs(initial_n)//(n1*n2))
  
    if initial_n < 0:
        while k >= (abs(initial_n)//(n1*n2)):
            if initial_n + k*n1*n2 > 0:
                return initial_n + k*n1*n2
            else:
                k += 1
                continue
    else:
        while k <= (abs(initial_n)//(n1*n2)):
            if initial_n - k*n1*n2 > 0:
                return initial_n - k*n1*n2
            else:
                k -= 1
                continue
        
    return "Not found"

print('\nThanks for reviewing')

# Thanks for reviewing
