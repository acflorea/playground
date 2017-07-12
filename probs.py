import matplotlib.pyplot as plt
import numpy as np

N = 300

# n
x = np.arange(0, N)

ts = N

y1 = np.zeros(N)
y2 = np.zeros(N)
y3 = np.zeros(N)

for i in x:
    y1[i] = 100 * np.float(i) / N * max(
        0.0, min(
            1.0, np.log(ts) - np.log(i)
        )
    )
    y2[i] = 100 * np.float(i) / N * max(
        0.0, min(
            1.0, np.log(float(ts)/2) - np.log(i)
        )
    )
    y3[i] = 100 * np.float(i) / N * max(
        0.0, min(
            1.0, np.log(float(ts)/3) - np.log(i)
        )
    )

plt.plot(x, y1, x, y2, x, y3)

plt.show()
