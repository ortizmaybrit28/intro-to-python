# Question 1: HOW MANY PLOTS 
import numpy as np 
import matplotlib.pyplot as plt

# Part 1: Define a function of a sinusoid with 3 arguements
def generate_sin_wave(x, A, w):
    return A * np.sin(w * x)

# Step 2: An array as x data from 0 to 2π with 1000 points
x = np.linspace(0, 2 * np.pi, 1000)

# Step 3: An array of  5 different amplitude values and wavelengths
amplitudes = [1, 2, 3, 4, 5]
wavelengths = [5, 4, 3, 2, 1]

# Step 4: Create a figure object
plt.figure(figsize=(10, 6))

# Step 5: Loop through each pair of A and w values and plot the corresponding y data
for idx, (A, w) in enumerate(zip(amplitudes, wavelengths), start=1):
    y = generate_sin_wave(x, A, w)
    plt.plot(x, y, label=f'Sine Function #{idx}')

plt.title('Sinusoids with Different Amplitudes and Wavelengths')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


# Question 2: RANDOMNESS
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate two lists of random numbers
np.random.seed(0)
data1 = np.random.randint(0, 101, 40)  
data2 = np.random.randint(0, 101, 40) 

# Step 2: Create a plot figure
plt.figure(figsize=(10, 6))

# Step 3: Plot the lines
plt.plot(data1, color='orange', linewidth=10, label='Orange line')
plt.plot(data2, color='red', linestyle='--', label='Red dashed line')

plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.show()

