
# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot
# f_output = []
# g_output = []
# def f(x):
#     return x

# def g(x):
#     return x + 1
# x_list = list(range(-3, 5))
# for x in x_list:
#   f_output.append(f(x))
#   g_output.append(g(x))
# pyplot.plot(x_list, f_output, x_list, g_output)
# pyplot.show()
# pyplot.savefig('myplot.png')
#pyplot.close() # start a new plot

# import matplotlib.pyplot as plot

# def f(x):
#     return x + 1

# xs = list(range(-3, 4))
# ys = []
# for x in xs:
#     ys.append(f(x))

# plot.plot(xs, ys)
# plot.show()

from turtle import *
import matplotlib
import matplotlib.pyplot as plot

def square():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

    plot.show()

square()