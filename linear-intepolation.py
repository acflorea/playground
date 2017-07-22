import collections


# function def
# points is a dictionary (x->y)
# x is float
def interpolate(points, x):
    # sort the x vector
    sortedXs = sorted(points)

    # if out of range - fail with error
    if x < sortedXs[0] or x > sortedXs[-1]:
        return "Buba! Out of range!!!"

    # attempt to find x1 and x2 so that x1 < x <= x2
    for index, xi in enumerate(sortedXs):
        if xi >= x:
            # found it
            x1 = sortedXs[index - 1]
            x2 = sortedXs[index]
            y1 = points[x1]
            y2 = points[x2]
            # compute the value for x
            return y1 + (y2 - y1) / (x2 - x1) * (x - x1)


# always make them floats (.0 trick)
points = {1.0: 1.0, 2.0: 4.0, 4.0: 16.0, 3.0: 9.0}

# method call
print interpolate(points, 2.5)
