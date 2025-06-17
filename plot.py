import numpy as np
import matplotlib.pyplot as plt

# Read file manually
time = []
voltage = []

with open('output.csv', 'r') as f:
    next(f)  # skip header
    for line in f:
        if line.strip() == '':
            continue  # skip empty lines
        t_str, v_str = line.split()
        
        # Convert time string to float (handle units like 'n', 'u')
        unit_multipliers = {'p':1e-12, 'n':1e-9, 'u':1e-6, 'm':1e-3}
        
        # time conversion
        for suffix, factor in unit_multipliers.items():
            if t_str.endswith(suffix):
                t = float(t_str.replace(suffix, '')) * factor
                break
        else:
            t = float(t_str)
        
        v = float(v_str)
        time.append(t)
        voltage.append(v)

# Convert to numpy arrays
time = np.array(time)
voltage = np.array(voltage)

plt.figure(figsize=(8,5))
plt.plot(time, voltage, label="V(out)")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("NGSpice Transient Simulation")
plt.grid()
plt.legend()
plt.savefig("plot.png")
print("Plot saved as plot.png")
