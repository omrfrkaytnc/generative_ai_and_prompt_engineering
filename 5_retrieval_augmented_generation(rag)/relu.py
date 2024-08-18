import matplotlib.pyplot as plt
import numpy as np

def relu(x):
  return np.maximum(0, x)

# Sample data
x = np.linspace(-5, 5, 100)

# Apply ReLU
y = relu(x)

# Plot 
plt.plot(x, y)
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('ReLU Activation Function')
plt.grid(True)
plt.show()
