
# rectangle
# ax.plot([top_left_x, top_left_x + width], [top_left_y, top_left_y], '--', linewidth=5, color='firebrick')
# ax.plot([top_left_x, top_left_x], [top_left_y, top_left_y + height], '--', linewidth=5, color='firebrick')
# ax.plot([top_left_x, top_left_x + width], [top_left_y + height, top_left_y + height], '--', linewidth=5,
#         color='firebrick')
# ax.plot([top_left_x + width, top_left_x + width], [top_left_y, top_left_y + height], '--', linewidth=5,
#         color='firebrick')

# ax.plot([50, 100], [200, 500], '--', linewidth=5, color='firebrick')

# ax.plot([x1, x2], [y1, y2], '--', linewidth=5, color='firebrick')


import matplotlib.pyplot as plt
import numpy as np


ax = plt.subplot(111)
t1 = np.arange(0.0, 1.0, 0.01)
for n in [1, 2, 3, 4]:
    plt.plot(t1, t1**n, label="n=%d"%(n,))

leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)

plt.show()