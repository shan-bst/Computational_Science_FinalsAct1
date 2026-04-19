import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#given data
time = np.array([0, 1, 2, 3, 4, 5])
position = np.array([0, 5, 15, 30, 50, 75])

# 1. Velocity using Central Difference
velocity = []
t_velocity = []

for i in range(1, len(time)-1):
    v = (position[i+1] - position[i-1]) / 2
    velocity.append(v)
    t_velocity.append(time[i])

velocity = np.array(velocity)
t_velocity = np.array(t_velocity)

# 2. Acceleration 
acceleration = []
t_acc = []

for i in range(1, len(velocity)-1):
    a = (velocity[i+1] - velocity[i-1]) / 2
    acceleration.append(a)
    t_acc.append(t_velocity[i])

# 3. Distance using Trapezoidal Rule
distance_est = sum((velocity[i] + velocity[i+1]) / 2 * (t_velocity[i+1] - t_velocity[i]) 
                   for i in range(len(velocity)-1))
actual_distance = position[-1] - position[0]

# Output results
print("Velocity Table:")
for t, v in zip(t_velocity, velocity):
    print(f"t = {t}s -> v = {v:.2f} m/s")

print("\nEstimated Distance (Trapezoidal):", round(distance_est, 2))
print("Actual Distance:", actual_distance)

# 4. Visualization
fig, ax = plt.subplots(2, 1, figsize=(8, 8))

# Position graph
ax[0].set_title("Position vs Time")
ax[0].set_xlim(0, 5)
ax[0].set_ylim(0, 80)
line1, = ax[0].plot([], [], marker='o')

# Velocity graph
ax[1].set_title("Velocity vs Time")
ax[1].set_xlim(1, 4)
ax[1].set_ylim(0, max(velocity)+5)
line2, = ax[1].plot([], [], marker='o', color='orange')

def update(frame):
    #position
    line1.set_data(time[:frame], position[:frame])
    
    #velocity
    if frame > 1:
        line2.set_data(t_velocity[:frame-1], velocity[:frame-1])
    
    return line1, line2

ani = FuncAnimation(fig, update, frames=len(time)+1, interval=800)

plt.tight_layout()
plt.show()