import numpy as np
import matplotlib.pyplot as plt

# Define the Maclaurin series function for sin(x)
def sin_maclaurin(x, n):
    s = 0
    for i in range(n):
        sign = (-1)**i
        term = x**(2*i+1) / np.math.factorial(2*i+1)
        s += sign*term
    return s

# Set the range of x values
x = np.linspace(0, 2*np.pi, 1000)

# Calculate sin(x) using the Maclaurin series with n=5
n = 5
sin_approx = sin_maclaurin(x, n)

# Plot the results
plt.plot(x, np.sin(x), label='Exact')
plt.plot(x, sin_approx, label='Maclaurin (n=5)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximation of sin(x) using Maclaurin series')
plt.legend()
plt.show()
