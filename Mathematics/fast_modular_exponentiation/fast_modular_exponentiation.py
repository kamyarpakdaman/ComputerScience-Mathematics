# In this program, we perform modular exponentiation using an efficient algorithm.
# We actually want to compute b^e (mod m).

# If e is an even integer, we can compute the result for each power and square it
# to jump to some powers up.

def FastModularExponentiationPowerTwo(b, k, m):
    
    step = b%m

    for _ in range(k):

        step = (step**2)%m
    
    return step

# If e is odd, we transform it into a sum of even and odd numbers and compute the final
# result usinf the algorithm for the even powers. E. g., 13 = 8 + 4 +1

def FastModularExponentiation(b, e, m):
    
    import math
  
    powers = []
    step = e
        
    while step > 1:
                
        tmp = 2**(math.log(step, 2)//1)
        powers.append(tmp)
        step = step - tmp
            
    multiple_parts = []
  
    for power in powers:
    
        PowerTwo = int(math.log(power, 2))
                
        multiple_parts.append(FastModularExponentiationPowerTwo(b, PowerTwo, m))
          
    result = 1
  
    for item in multiple_parts:
    
        result *= item
        
    if e%2 == 0:
                
        return result%m
    
    else:
        
        result *= b
                
        return result%m

print('\nThanks for reviewing')

# Thanks for reviewing
