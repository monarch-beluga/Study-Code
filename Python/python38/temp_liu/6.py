
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.array(range(1,10))
y = x*3
plt.tick_params(bottom=False)
plt.plot(x, y, color='k', label='A')
plt.legend(loc=9, bbox_to_anchor=(0.5, 1.1))
