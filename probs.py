import matplotlib.pyplot as plt
import numpy as np

N = 300

# n
x = np.arange(1, N + 1)

ts = N

y1 = np.zeros(N)
yt = np.zeros(N)

z1 = np.zeros(N)
zt = np.zeros(N)

for i in x:
    y1[i - 1] = np.float(i) / N * (np.log(ts) - np.log(i))
    yt[i - 1] = np.float(i) / ts + \
                (1 - np.float(i) / ts) * np.float(i) / N * (np.log(ts) - np.log(i))

    z1[i - 1] = np.float(i) / (N * (ts - 1)) * (float(ts - 1 - i + np.log(ts - 1) - np.log(i)))
    # find the max among first m items
    # max is the first item found after m items
    # max is not the first item found after m items but the second one
    zt[i - 1] = np.float(i) / ts + \
                (1 - np.float(i) / ts) * (y1[i - 1] + \
                                          (1 - y1[i - 1]) * (np.float(i) / (N * (ts - 1)) * (
                                              float(ts - 1 - i + np.log(ts - 1) - np.log(i)))))

y1p, = plt.plot(x, y1, 'r', label="k=0 - P(Find opt and stop early)")
y1pt, = plt.plot(x, yt, 'r--', label="k=0 - P(Find opt regardless of early stopping)")
z1p, = plt.plot(x, z1, 'b', label="k=1 - P(Find opt and stop early)")
z1pt, = plt.plot(x, zt, 'b--', label="k=1 - P(Find opt regardless of early stopping)")

plt.legend(handles=[y1p, y1pt, z1p, z1pt])

plt.show()
