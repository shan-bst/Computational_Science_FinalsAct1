import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

color_bg = "#121926"      
color_energy = "#3b82f6"  
color_power = "#ef4444"   
color_highlight = "#ffffff" 
color_grid = "#2d3748"

plt.rcParams['axes.facecolor'] = color_bg
plt.rcParams['figure.facecolor'] = color_bg
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

time = np.array([0, 2, 4, 6, 8, 10]) # hours
energy = np.array([0.0, 1.5, 3.5, 6.0, 9.0, 13.0]) # kWh

h = 2 
power = []
t_power = []

for i in range(1, len(time)-1):
    p_val = (energy[i+1] - energy[i-1]) / (2 * h)
    power.append(p_val)
    t_power.append(time[i])

total_energy_est = 0
for i in range(len(time)-1):
    area = ((energy[i] + energy[i+1]) / 2) * (time[i+1] - time[i])
    total_energy_est += area

print("--- CASE STUDY 5 RESULTS ---")
print("Power Consumption Table:")
for t, p in zip(t_power, power):
    print(f"Time {t}h: Power = {p:.3f} kW")

print(f"\nTotal Energy (Integrated): {total_energy_est:.2f} kWh")
print(f"Actual Final Energy: {energy[-1]} kWh")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Energy vs Time
ax1.plot(time, energy, color=color_energy, marker='o', linewidth=3, 
         markersize=10, markerfacecolor=color_highlight)
ax1.set_title('Energy Consumption (kWh)', fontsize=14, fontweight='bold', color=color_highlight)
ax1.set_xlabel('Time (hours)', fontweight='bold')
ax1.set_ylabel('Energy (kWh)', fontweight='bold')
ax1.grid(True, color=color_grid, alpha=0.6)

for i, val in enumerate(energy):
    ax1.annotate(f"{val}k", (time[i], energy[i]), textcoords="offset points", 
                 xytext=(0,15), ha='center', fontweight='bold')

# Subplot 2: Power vs Time
ax2.plot(t_power, power, color=color_power, marker='o', linewidth=3, 
         markersize=10, markerfacecolor=color_highlight)
ax2.set_title('Instantaneous Power (kW)', fontsize=14, fontweight='bold', color=color_highlight)
ax2.set_xlabel('Time (hours)', fontweight='bold')
ax2.set_ylabel('Power (kW)', fontweight='bold')
ax2.grid(True, color=color_grid, alpha=0.6)

for i, val in enumerate(power):
    ax2.annotate(f"{val:.2f}", (t_power[i], power[i]), textcoords="offset points", 
                 xytext=(0,15), ha='center', fontweight='bold')

for ax in [ax1, ax2]:
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.suptitle('Electricity Consumption and Power Analysis', fontsize=16, fontweight='bold', color='white')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()