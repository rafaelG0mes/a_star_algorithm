
import graph
from numpy import *

class Node:
  # Class to handle the paramters of the nodes
  def __init__(self, position, parent):
    self.position = position
    self.parent = parent
    self.g = float("inf")
    self.h = float("inf")
    self.f = float("inf")
  
class myPathPlanning:
  def __init__(self, grid, start, stop, graphic):

    self.grid = grid
    self.start = Node(start, None)
    self.stop = Node(stop, None)

    self.path = []
    self.openlist = []
    self.closedlist = []

    self.openlist.append(self.start) 
    self.weight = 5 # Used to optmize the search

    # Starts the algorithm
    self.run()   

  def get_distance (self, a, b):
    (x1, y1) = a
    (x2, y2) = b
    # return (abs(x1 - x2) + abs(y1 - y2))    # Manhatam distance
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5 # Euclidean distance

  def check_closedlist(self, node):
    # Checks if the node is in the closedlist
    for check in self.closedlist:
      if node.position == check.position:
        return True

  def check_open(self, node):
    # Checks if the node can be added to the openlist
    for check in self.openlist:
      if node.position == check.position and node.f >= check.f:
        return False
    return True

  def check_limits(self, node):
    # Checks if the neighbors are within the grid (and are not obstacles)
    (width, length) = shape(self.grid)
    (nx, ny) = node
    if (nx >= 0 and ny >= 0 and nx < width and ny < length and grid[nx][ny] != 1):
      return True

  def get_path(self):
    # Returns the path generated
    return self.path
  
  def sort_list(self):
    '''
    Sorts the openlist with the following rules:
    - Take the node with the least value of F.
      If there's a tie:
      - Take the node with the least value of H (that means, closer to the goal)
        If there's a tie:
        - Take the node with the greater value of G (that means, farther from the start)
    '''
    if self.openlist:
      # Sort list according to the F paramter
      sortF = sorted(self.openlist, key=lambda x: x.f) 
      sortF = [elem for elem in sortF if elem.f == sortF[0].f]
      # Sort list according to the H paramter
      sortH = sorted(sortF, key=lambda x: x.h) 
      sortH = [elem for elem in sortH if elem.h == sortH[0].h]
      # Sort list according to the G paramter
      sortG = sorted(sortF, key=lambda x: x.g, reverse = True) 
      sortG = [elem for elem in sortG if elem.g == sortG[0].g]
    # returns the node with the best score      
    return sortG[0]

  def path_reconstruction(self, current_node):
    # Backwards step, using parent information
    while current_node.parent:
      self.path.append(current_node.position)
      current_node = current_node.parent
    self.path.append(self.start.position)
    self.path.reverse()
    
    # Graphical part
    for node in self.path:
      graphic.update_grid(node, 'blue')
    graphic.update_grid(self.start.position, 'yellow')
    graphic.update_grid(self.stop.position, 'yellow')
    graphic.show_grid(True)       

  # A star path planner
  def run (self):
    """
    - grid  : List of Lists : Row[Col[]]. Possible values : 0 or 1
    - start : Couple representing start cell coordinates. For example (4,0)
    - stop  : Couple representing stop cell coordinates. For example (0,4)
    """
    # While the open set is not empty
    while self.openlist: 
      current_node = self.sort_list()
      self.openlist.pop(self.openlist.index(current_node))
      
      self.closedlist.append(current_node)
      graphic.update_grid(current_node.position, 'red')
      
      # Stops if the current node is the end node
      if current_node.position == self.stop.position:
        self.path_reconstruction(current_node)
        break

      # Evaluate neighbors.
      # I didn't consider the neighbors in the diagonal cases, only the adjacent ones
      (x,y) = current_node.position
      neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
      
      for node in neighbors:
        # Verifies if the new node is within the boundaries
        if self.check_limits(node):
          new_node = Node(node, current_node)

          # Verifies if the node is in the closed list
          if self.check_closedlist(new_node):
            continue
          
          # Assigns the values of F, G and H for the node
          new_node.g = self.get_distance (new_node.position, self.start.position)
          new_node.h = self.get_distance (new_node.position, self.stop.position)*self.weight
          new_node.f = new_node.g + new_node.h

          if self.openlist:
            # Verifies if the node can be added to the open list
            if self.check_open(new_node):
              self.openlist.append(new_node)
              graphic.update_grid(new_node.position, 'green')
          else:
            # If the openlist is empty, add the node to it
            self.openlist.append(new_node)
            graphic.update_grid(new_node.position, 'green')      

      graphic.show_grid(False)
      
    if not(self.path):
      print ("Couldn't find a path")

if __name__ == "__main__":

  """
  Exemple 1: How to reach the cell (0,4) starting from (4,0)
  """
  # Configuration for the example 1
  grid = [  [1,0,1,0,0],
            [0,0,0,0,1],
            [1,0,1,1,0],
            [0,0,0,0,0],
            [0,1,0,1,0]]
  start = (4,0)
  stop = (0,4)

  """
  Exemple 2: How to reach the cell (19,0) starting from (12,16)
  """
  # Configuration for the example 2
  grid =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,],
          [1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,],
          [1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,],
          [1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1,],
          [1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,],
          [1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,],
          [1,0,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,],
          [1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,],
          [1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,],
          [1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,],
          [1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,],
          [1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,],
          [1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,],
          [1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,],
          [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,],
          [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],]
  start = (19,0)
  stop = (12,16)


  ts = 1e-7 #seconds
  # Initializes the graphic object
  graphic = graph.graphic(grid, start, stop, ts)
  # Initializes the Path planner object
  path = myPathPlanning (grid, start, stop, graphic)
  # shows the path planned
  print (path.get_path())

