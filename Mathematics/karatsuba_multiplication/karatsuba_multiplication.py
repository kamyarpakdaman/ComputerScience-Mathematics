# In this program, we're going to perform the Karatsuba multiplication using a Divide and Conquer approach; 
# which is more efficient than the method we already know from the 3rd grade school.

# In Karatsuba multiplication of X = 5678 and Y = 1234, we define a = 56, b = 78, c = 12, d = 34, and n = 4. Actually, 
# a, b, c, and d are halves of the original numbers and n is the maximum length of X and Y. We use the maximum length
# to ensure that in each recursion, the larger number is broken into smaller numbers, until we reach our base case of
# X and Y less than 10.

# X = 10**(n/2)*a + b and Y = 10**(n/2)*c + d
# Therefore:
# X*Y = 10**n*(a*c) + 10**(n/2)*(a*d + b*c) + b*d

# Then, we recursively compute a*c and b*d. But, instead of computing a*d and b*c, we compute (a+b)*(c+d) and subtract
# a*c and b*d from it to get (a*d + b*c). Hence, through recursively computing three multiplications, we finally get
# to the result of our first multiplication.

def karatsuba_mult(X, Y):

    from math import ceil, floor
    
    # This is our base case.

    if X < 10 and Y < 10:
        return X * Y

    # Determining the size of X and Y to find n.

    size = max(len(str(X)), len(str(Y)))
    n = ceil(size // 2)

    # Splitting X and Y using n and power of 10.
    # Note that in this step, if one number is large and the other is small, it might be the case that the smaller
    # number remains unchanged until the larger one gets close enough. E.g., if X = 32658997 and Y = 235, Y will
    # remain 235 until X gets to, say, 997.

    p = 10 ** n
    a = floor(X // p)
    b = X % p
    c = floor(Y // p)
    d = Y % p

    # Recursively computing the multiplications.

    ac = karatsuba_mult(a, c)
    bd = karatsuba_mult(b, d)
    e = karatsuba_mult(a + b, c + d) - ac - bd

    # Returning the multiplication result in each recursion.
    return int(10 ** (2 * n) * ac + (10 ** n) * e + bd)

print('\nThanks for reviewing')

# Thanks for reviewing
