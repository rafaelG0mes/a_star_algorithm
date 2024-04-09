from   numpy      import *
from   matplotlib import colors
import matplotlib.pyplot as plt
import numpy             as np

class graphic:
  def __init__(self, grid,start, stop, ts):
    self.start = start
    self.stop = stop
    self.grid = grid

    self.ts = ts
    self.color = ['white', 'yellow', 'green', 'red', 'blue', 'black']
    self.color_dic = {}
    for i in range(len(self.color)):
      self.color_dic[self.color[i]] = i/5.

    self.grid[start[0]][start[1]] = self.color_dic['yellow']
    self.grid[stop[0]][stop[1]] = self.color_dic['yellow']

    self.fig, self.ax = plt.subplots()
    self.ax.set_title('Mypath planner')
    self.initialize()

  def show_grid(self, hold):
    plt.cla()
    self.ax.set_title('Mypath planner')
    self.ax.imshow(self.grid, cmap=self.cmap, interpolation='nearest', extent=[0,self.width,0,self.length])
    # draw gridlines
    self.ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=0.3)
    self.ax.set_xticks(np.arange(0, self.width, 1))
    self.ax.set_yticks(np.arange(0, self.length, 1))

    if hold:
      plt.show()
    else:
      plt.draw()
      plt.pause(self.ts)

  def update_grid(self, node, color):
    (x,y) = node
    self.grid[x][y] = self.color_dic[color]

  def initialize(self):
    # create discrete colormap
    self.cmap = colors.ListedColormap(self.color)
    bounds = [0,30,30]
    (self.length, self.width) = shape(self.grid)
    self.ax.imshow(self.grid, cmap=self.cmap, interpolation='nearest', extent=[0,self.width,0,self.length])

    # draw gridlines
    self.ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=0.3)
    self.ax.set_xticks(np.arange(0, self.width, 1))
    self.ax.set_yticks(np.arange(0, self.length, 1))


