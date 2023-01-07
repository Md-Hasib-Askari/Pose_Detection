# from scipy.ndimage.filters import gaussian_filter1d
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import matplotlib

matplotlib.use('TkAgg')
# style.use('TkAgg')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    graph_data = open('data.csv', 'r').readlines()
    # lines = graph_data.split(',')
    xs = []
    ys = []

    for line in graph_data:
        if len(line) > 1:
            x, y = line.split(',')
            if x == 'x' or float(x) < 0:
                continue
            x = float(x)
            y = float(y)
            # ysmoothed = gaussian_filter1d(y, sigma=2)
            xs.append(x)
            ys.append(y)
            print(x, y)

    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()
