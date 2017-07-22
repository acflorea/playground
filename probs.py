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

plt.plot(x, y1, 'r')
plt.plot(x, yt, 'r--')
plt.plot(x, z1, 'g')
plt.plot(x, zt, 'g--')
# plt.plot(x, 0.5 * y1 + 0.5 * z1, 'b')
# plt.plot(x, 0.5 * yt + 0.5 * zt, 'b--')

plt.show()
