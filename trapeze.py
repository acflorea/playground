from math import sin, pi


def trapezoidal(f, a, b, n):
    if a > b:
        print ('Incorrect bounds')
        return None
    h = float(b - a) / n
    s = f(a)
    for i in range(1, n):
        s += 2 * f(a + i * h)
    s += f(b)
    return s * h / 2.0


print(trapezoidal(lambda x: sin(x), 0, pi, 8))
