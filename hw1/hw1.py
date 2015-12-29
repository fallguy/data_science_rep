
""" 
# DAT-LA-08: Homework 1
#
# Linear Regression
#
# FEEDBACK: Great job! Clear, easy-to-read code. In general, work on
#   adding whitespace. Placing spaces around lower-precedence operators
#   is part of PEP8. Also, placing spaces inbetween lines (see the 
#   mammal_data function) would help a lot with code readability.
#
#
# Uppercase single letters indicate vectors.
# Lowercase single letters indicate scalars.
"""

import os
import csv
from math import log
from matplotlib import pyplot as plt

# Points for testing.
# Consists of the two points: [(0, 2), (1, 4)]
# What do you expect to get for m and b?
X_test = [0, 1]
Y_test = [2, 4]

# Homework data. What are m and b?
# Consists of the points: [(15.52, 19.93), (4.10, 3.55), ...]
X = [15.52, 4.10, 64.47, 11.71, 99.21, 
     30.75, 41.15, 38.15, 3.69, 94.28]

Y = [19.93, 3.55, 56.73, 10.67, 81.99, 
     36.74, 38.14, 30.52, 7.60, 96.54]


def plot_model(X, Y, m, b, n):
    """ Draw scatter plot of data points and
        the predicted line y = mx + b. """
    plt.cla()
    plt.scatter(X, Y, color='r')
    plt.plot((min(X),max(X)),
             (m*min(X) + b, m*max(X) + b),
                color='b')
    plt.title('Best fit line')
    plt.xlabel('x')
    plt.ylabel('y')
    savefile='out' + n + '.png'
    plt.savefig(savefile)
    print('Saved figure to {}'
        .format(os.path.dirname(os.path.realpath(__file__))
        +'/'+savefile))
    plt.close()


def mean(nums):
    """ Returns mean value of nums. """
    
    m = sum(nums)/len(nums)
    
    return m


def intercept(X, Y, m):
    """ Given data points (xi, yi) and slope m, 
    returns the y-intercept of the best-fit line. """

    # Nice job reusing mean()!
    # Place spaces around lower-precedence operators such as '-'.
    b = mean(Y) - m*mean(X)

    return b


def slope(X, Y):
    """ Given data points (xi, yi), returns
    the slope m of the best-fit line. """

    # Excellent, but try doing these as list comprehensions --
    #   will result in slightly cleaner code. But, this is a clever
    #   way instead of using zip()
    xy = sum(list(map(lambda x,y: x*y,X,Y)))
    x2 = sum(list(map(lambda x: x*x,X)))

    # Put spaces around operators with lower precedence.
    #  Also, unclear whether * or **2 is applied first,
    #    so use parentheses to make it clear.
    m = (xy - len(X)*mean(X)*mean(Y))/(x2 - len(X)*(mean(X)**2))
    
    return m

def mammal_data(file):

    # Nice! Consider always specifying 'r' and encoding
    with open(file, 'r') as f:
        r = csv.DictReader(f)

        X_body=[]
        Y_brain=[]
        for line in r:
            X_body.append(float(line['body']))
            Y_brain.append(float(line['brain']))
    
    # Nice job applying log to each entry
    X_log = [log(x) for x in X_body]
    Y_log = [log(y) for y in Y_brain]

    return X_body,Y_brain, X_log, Y_log


# TEST the mean function
print("mean([0, 1]) => ", mean(X_test))
print("mean([2, 4]) => ", mean(Y_test))

# More tests
#
#
#

# Test linear regression on points: [(0, 2), (1, 4)]
m = slope(X_test, Y_test)
b = intercept(X_test, Y_test, m)
plot_model(X_test, Y_test, m, b, '0')

# Fit and plot model for actual X and Y
m = slope(X, Y)
b = intercept(X, Y, m)
plot_model(X, Y, m, b, '1')

print()
print("Slope (m): {}".format(m))
print("Intercept (b): {}".format(b))
print("Model: y = {}x + {}".format(m, b))

file = 'hw1-mammals.csv'
X_body, Y_brain, X_log, Y_log = mammal_data(file)

m = slope(X_body, Y_brain)
b = intercept(X_body, Y_brain, m)
plot_model(X_body, Y_brain, m, b, '2')

print()
print("Mammal Slope (m): {}".format(m))
print("Mammal Intercept (b): {}".format(b))
print("Mammal Model: y = {}x + {}".format(m, b))

m2 = slope(X_log, Y_log)
b2 = intercept(X_log, Y_log, m2)
plot_model(X_log, Y_log, m2, b2, '3')

print()
print("Mammal Slope (m): {}".format(m2))
print("Mammal Intercept (b): {}".format(b2))
print("Mammal Model: log(y) = {}x + {}".format(m2, b2))



