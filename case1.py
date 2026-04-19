import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

color_bg = "#121926"
color_b = "#3b82f6"   
color_g = "#059669"   
color_w = "#ffffff"   
color_grid = "#2d3748"

years = [2020, 2021, 2022, 2023, 2024]
population = [10000, 10800, 11900, 13200, 14800]
growth_rates = [np.nan, 950, 1200, 1450, np.nan]

plt.rcParams['axes.facecolor'] = color_bg
plt.rcParams['figure.facecolor'] = color_bg
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Population vs Time (LEFT)
ax1.plot(years, population, color=color_b, marker='o', linewidth=3, markersize=10, markerfacecolor=color_w)
ax1.set_title('Population Growth (EXPONENTIAL)', fontsize=14, fontweight='bold', color=color_w)
ax1.set_xlabel('Year', fontweight='bold')
ax1.set_ylabel('Population', fontweight='bold')
ax1.grid(True, color=color_grid, alpha=0.6)

# Labeling Population
for i, val in enumerate(population):
    ax1.annotate(str(val), (years[i], population[i]), textcoords="offset points", xytext=(0,15), ha='center', fontweight='bold')

# Growth Rate vs Time (RIGHT)
ax2.plot(years, growth_rates, color=color_g, marker='o', linewidth=3, markersize=10, markerfacecolor=color_w)
ax2.set_title('Growth Rate (Accelerating)', fontsize=14, fontweight='bold', color=color_w)
ax2.set_xlabel('Year', fontweight='bold')
ax2.set_ylabel('Growth Rate (people/year)', fontweight='bold')
ax2.grid(True, color=color_grid, alpha=0.6)

# Labeling Growth Rate
for i, val in enumerate(growth_rates):
    if not np.isnan(val):
        ax2.annotate(str(int(val)), (years[i], growth_rates[i]), textcoords="offset points", xytext=(0,15), ha='center', fontweight='bold')

for ax in [ax1, ax2]:
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.suptitle('Population Analysis Results', fontsize=16, fontweight='bold', color='white')
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust for suptitle
plt.show()