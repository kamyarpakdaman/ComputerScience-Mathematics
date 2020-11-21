# a*X + b*Y = c has a solution of integers if and only if gcd(a, b)|c
# The doiphantine function below computes X and Y such that above conditions
# hold.

# This function computes the Greatest Common Divisors of two integers efficiently.

def gcd(a, b):
      
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        
        if a >= b:
            a = a % b
        else:
            b = b % a
    
    return max(a, b)

# This function computes d, X, and Y such that:
# d = gcd(a, b) and d = a*X + b*Y

def extended_gcd(a, b):

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    
    return (d, x, y)

# Finally, this function computes X and Y such that the diophantine conditions 
# hold.

def diophantine(a, b, c):
      
    assert c % gcd(a, b) == 0
    
    d, x0, y0 = extended_gcd(a, b)

    mult = c/d
    x = x0 * mult
    y = y0 * mult

    return (x, y)

print('\nThanks for reviewing')

# Thanks for reviewing
