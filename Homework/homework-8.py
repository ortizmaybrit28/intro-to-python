# 1) CURVE FITTING GUIDED PROBLEM
# PART 1A
import pandas as pd

file_path = "GlobalLandTemperaturesByState.csv" 
df = pd.read_csv(file_path)
filtered_df = df[['dt', 'AverageTemperature', 'State']]
filtered_df['dt'] = pd.to_datetime(filtered_df['dt'])
filtered_df = filtered_df[filtered_df['dt'].dt.year > 2000]
states_to_include = ['Wyoming', 'Nebraska', 'South Dakota']
filtered_df = filtered_df[filtered_df['State'].isin(states_to_include)]
print(filtered_df.shape)  
print(filtered_df.head())


# PART 1B
import pandas as pd

file_path = "GlobalLandTemperaturesByState.csv"  
df = pd.read_csv(file_path)
df['dt'] = pd.to_datetime(df['dt'])
filtered_df = df[['dt', 'AverageTemperature', 'State']]
filtered_df = filtered_df[filtered_df['dt'].dt.year > 2000]
states_to_include = ['Wyoming', 'Nebraska', 'South Dakota']
filtered_df = filtered_df[filtered_df['State'].isin(states_to_include)]
average_temperature_by_date = filtered_df.groupby('dt')['AverageTemperature'].mean().reset_index()
average_temperature_by_date.columns = ['date', 'average_temperature']
print(average_temperature_by_date)


# PART 1C
import matplotlib.pyplot as plt

print(filtered_df.columns)
plt.figure(figsize=(12, 6))
for state in states_to_include:
    state_data = filtered_df[filtered_df['State'] == state]
    plt.plot(state_data['dt'], state_data['AverageTemperature'], label=state)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)
plt.title('Average Land Temperatures in Wyoming, Nebraska, and South Dakota (Post-2000)', fontsize=14)
plt.legend(title="State", 
    fontsize=10, 
    title_fontsize=12, 
    loc='upper left', 
    bbox_to_anchor=(1, 1)
)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# PART 1D
import pandas as pd

filtered_df['dt'] = pd.to_datetime(filtered_df['dt'])  
filtered_df['DateNumeric'] = filtered_df['dt'].apply(lambda x: x.timestamp())
print(filtered_df[['dt', 'DateNumeric']].head())

# PART 1E
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

df = pd.read_csv('GlobalLandTemperaturesByState.csv')
df['Date'] = pd.to_datetime(df['dt'])
df = df[df['Date'].dt.year > 2000]
df = df[df['State'].isin(['Wyoming', 'Nebraska', 'South Dakota'])]
x_data = (df['Date'] - df['Date'].min()).dt.days
y_data = df['AverageTemperature']
def model_equation(x, A, f, phi, b):
    return A * np.cos(2 * np.pi * f * x + phi) + b
initial_guess = [10, 0.5, 0, 0]
params, covariance = curve_fit(model_equation, x_data, y_data, p0=initial_guess)
A_fit, f_fit, phi_fit, b_fit = params
print("Fitted parameters:")
print(f"Amplitude (A): {A_fit}")
print(f"Frequency (f): {f_fit}")
print(f"Phase (phi): {phi_fit}")
print(f"Offset (b): {b_fit}")
fitted_curve = model_equation(x_data, *params)
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label="Observed Data", alpha=0.5)
plt.plot(x_data, fitted_curve, color="red", label="Fitted Curve")
plt.xlabel("Date (Days from Start)")
plt.ylabel("Average Temperature (°C)")
plt.title("Temperature Trends After 2000 in Wyoming, Nebraska, and South Dakota")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()


# PART 1F
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

df = pd.read_csv('GlobalLandTemperaturesByState.csv')
df['Date'] = pd.to_datetime(df['dt'])
df = df[df['Date'].dt.year > 2000]
df = df[df['State'].isin(['Wyoming', 'Nebraska', 'South Dakota'])]
x_data = (df['Date'] - df['Date'].min()).dt.days
y_data = df['AverageTemperature']
print(df.head())
print(x_data.head())
print(y_data.head())
print(df.shape)
def model_equation(x, A, f, phi, b):
    return A * np.cos(2 * np.pi * f * (x - x.min()) / (x.max() - x.min()) + phi) + b
initial_guess = [10, 0.5, 0, 0]
params, covariance = curve_fit(model_equation, x_data, y_data, p0=initial_guess)
A_fit, f_fit, phi_fit, b_fit = params
print("Fitted parameters:")
print(f"Amplitude (A): {A_fit}")
print(f"Frequency (f): {f_fit}")
print(f"Phase (phi): {phi_fit}")
print(f"Offset (b): {b_fit}")
fitted_curve = model_equation(x_data, *params)
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label="Observed Data", alpha=0.5)
plt.plot(x_data, fitted_curve, color="red", label="Fitted Curve")
plt.xlabel("Date (Days from Start)")
plt.ylabel("Average Temperature (°C)")
plt.title("Temperature Trends After 2000 in Wyoming, Nebraska, and South Dakota")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()


# PART 1G
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

df = pd.read_csv('GlobalLandTemperaturesByState.csv')
df['Date'] = pd.to_datetime(df['dt'])
df = df[df['Date'].dt.year > 2000]
df = df[df['State'].isin(['Wyoming', 'Nebraska', 'South Dakota'])]
x_data = (df['Date'] - df['Date'].min()).dt.days  # Days from start
y_data = df['AverageTemperature']  # Temperature values
def model_equation(x, A, f, phi, b):
    return A * np.cos(2 * np.pi * f * (x - x.min()) / (x.max() - x.min()) + phi) + b
initial_guess = [10, 0.5, 0, 0]  # Example guess
params, covariance = curve_fit(model_equation, x_data, y_data, p0=initial_guess)
A_fit, f_fit, phi_fit, b_fit = params
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label="Observed Data", alpha=0.5)
fitted_curve = model_equation(x_data, *params)
plt.plot(x_data, fitted_curve, color="red", label="Fitted Curve")
plt.xlabel("Date (Days from Start)")
plt.ylabel("Average Temperature (°C)")
plt.title("Temperature Trends After 2000 in Wyoming, Nebraska, and South Dakota")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# PART 1H
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

df = pd.read_csv('GlobalLandTemperaturesByState.csv')
df['Date'] = pd.to_datetime(df['dt'])
df = df[df['Date'].dt.year > 2000]
df = df[df['State'].isin(['Wyoming', 'Nebraska', 'South Dakota'])]
x_data = (df['Date'] - df['Date'].min()).dt.days  # Days from start
y_data = df['AverageTemperature']  # Temperature values
def model_equation(x, A, f, phi, b):
    return A * np.cos(2 * np.pi * f * (x - x.min()) / (x.max() - x.min()) + phi) + b
initial_guess = [10, 0.5, 0, 0]  # Example guess
params, covariance = curve_fit(model_equation, x_data, y_data, p0=initial_guess)
A_fit, f_fit, phi_fit, b_fit = params
errors = np.sqrt(np.diag(covariance))
print("Fitted parameters:")
print(f"Amplitude (A): {A_fit} ± {errors[0]}")
print(f"Frequency (f): {f_fit} ± {errors[1]}")
print(f"Phase (phi): {phi_fit} ± {errors[2]}")
print(f"Offset (b): {b_fit} ± {errors[3]}")
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label="Observed Data", alpha=0.5)
fitted_curve = model_equation(x_data, *params)
plt.plot(x_data, fitted_curve, color="red", label="Fitted Curve")
plt.xlabel("Date (Days from Start)")
plt.ylabel("Average Temperature (°C)")
plt.title("Temperature Trends After 2000 in Wyoming, Nebraska, and South Dakota")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# PART 1I
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

df = pd.read_csv('GlobalLandTemperaturesByState.csv')
df['Date'] = pd.to_datetime(df['dt'])
df = df[df['Date'].dt.year > 2000]
df = df[df['State'].isin(['Wyoming', 'Nebraska', 'South Dakota'])]
x_data = (df['Date'] - df['Date'].min()).dt.days  
y_data = df['AverageTemperature'] 
def model_equation(x, A, f, phi, b):
    return A * np.cos(2 * np.pi * f * (x - x.min()) / (x.max() - x.min()) + phi) + b
initial_guess = [10, 0.5, 0, 0]  
params, covariance = curve_fit(model_equation, x_data, y_data, p0=initial_guess)
A_fit, f_fit, phi_fit, b_fit = params
errors = np.sqrt(np.diag(covariance))
print(f"Amplitude (A): {A_fit:.3f} ± {errors[0]:.3f}")
print(f"Frequency (f): {f_fit:.3f} ± {errors[1]:.3f}")
print(f"Phase (phi): {phi_fit:.3f} ± {errors[2]:.3f}")
print(f"Offset (b): {b_fit:.3f} ± {errors[3]:.3f}")
final_equation = f"{A_fit:.3f} * cos(2π * {f_fit:.3f} * (x - {x_data.min()}) / ({x_data.max()} - {x_data.min()}) + {phi_fit:.3f}) + {b_fit:.3f}"
print(f"Final equation: {final_equation}")
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label="Observed Data", alpha=0.5)
fitted_curve = model_equation(x_data, *params)
plt.plot(x_data, fitted_curve, color="red", label="Fitted Curve")
plt.xlabel("Date (Days from Start)")
plt.ylabel("Average Temperature (°C)")
plt.title("Temperature Trends After 2000 in Wyoming, Nebraska, and South Dakota")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()



# 2) RANDOM PLOTTING PRACTICE
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
list1 = np.random.randint(0, 201, 50)
list2 = np.random.randint(0, 201, 50)
list3 = np.random.randint(0, 201, 50)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(list1, color='blue', linewidth=5, label='List 1 (Blue Line)')
plt.plot(list2, linestyle='--', color='green', label='List 2 (Green Dotted Line)')
plt.title('Random Data Lines')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend(bbox_to_anchor=(1, 1))
plt.subplot(1, 2, 2)
plt.scatter(range(len(list3)), list3, color='purple', marker='^', label='List 3 (Purple Triangles)')
plt.title('Random Data Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend(bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()



# 3) MONTE CARLO
import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(N):
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    distances = x**2 + y**2
    inside_circle = distances <= 1
    pi_estimate = 4 * np.sum(inside_circle) / N
    return pi_estimate, x, y, inside_circle
Ns = [10**1, 10**3, 10**5, 10**6]
estimates = [estimate_pi(N) for N in Ns]
N = 10**4
pi_estimate, x, y, inside_circle = estimate_pi(N)
plt.figure(figsize=(6, 6))
plt.scatter(x[inside_circle], y[inside_circle], color='blue', alpha=0.5, label='Inside Quarter Circle')
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', alpha=0.5, label='Outside Quarter Circle')
plt.text(0, -0.8, f'Estimated π = {pi_estimate:.5f}', fontsize=12, ha='center')
plt.title(f'Estimate of π with N={N}')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.show()
for N, (pi_est, _, _, _) in zip(Ns, estimates):
    print(f"Estimate of π with N={N}: {pi_est:.5f}")
'''
As the number of random points (N) goes up, the estimate of π becomes more accurate.
Using random sampling gives a better approximation of π because it increases
the reliability of the results and reduces the impact of random chances.
'''
