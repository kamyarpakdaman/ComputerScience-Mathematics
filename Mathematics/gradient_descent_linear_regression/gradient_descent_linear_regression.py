# In this program we use the Gradient Descent method for performing Linear Regression.

import matplotlib.pyplot as plt

# Using this function, we find the gradient when b has a specific value.

def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

# Using this function, we find the gradient when m has a specific value.

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

# In this function, at any given (b, m) pair, we find the gradients, and using them, we modify b and m.

def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]
  
# Finally, using this function, we perform the step_gradient function for a number of times to improve
# b and m values.
 
def gradient_descent(x, y, learning_rate, num_iterations):
  b = 0
  m = 0
  for _ in range(num_iterations):
    b, m = step_gradient(b, m, x, y, learning_rate)
  return [b,m]  

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

b, m = gradient_descent(months, revenue, 0.01, 1000)

y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()

print('\nThanks for reviewing')

# Thanks for reviewing
