import matplotlib.pyplot as plt
from math import pi,sin

# Data for plotting
L = 100
time = list(range(L))
Voltage = [sin(2*pi*t/L) for t in time]

fig, ax = plt.subplots()
ax.plot(time, Voltage)

ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='Example 1')
ax.grid()

fig.savefig("test.png")
plt.show()
