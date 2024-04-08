Subject
-----

Here's a little game for you. In the following grid :
- Black cells are obstacles.
- You can walk on all the yellow cells
- You need to write an algorithm that gets you from a start cell to a stop cell.

For example, how would you reach the cell R:0, C:4 if you started from R: 4, C:0 ? 

```
Input : Grid Matrix, start & stop
Output : Path planning algorithm
```
```
grid = [[ 1,0,1,0,0 ],
        [ 0,0,0,0,1 ],
        [ 1,0,1,1,0 ],
        [ 0,0,0,0,0 ],
        [ 0,1,0,1,0 ]]
```
```
def myPathPlanning (grid, start, stop):
"""
- grid : List of Lists : Row[Col[]]. Possible values : 0 or 1
- start : Couple representing start cell coordinates. For example (4,0)
- stop : Couple representing stop cell coordinates. For example (0,4)
""" 
```


Solution proposed
-----

The code in this repository contains the solution proposed to plan the trajectory to go from a point to another in a given grid. The solution was inspired by a well-known algorithm for this kind of problem, the [A* algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm).

Since the path to be analyzed is discretized, we can solve the problem using algorithms based on graphs. That is, it is possible to perform the analysis by estimating the cost associated with the nodes at the edges of the possible paths and choosing the path that has the lowest cost.

**The A\* algorithm**

**1. Introduction**

Algorithm A * is an algorithm used to find the shortest path between a start node and an end node within a graph, and it is not necessary to explore all possible paths. This algorithm represents an extension of Dijkstra's algorithm that explores all path possibilities before choosing the best one possible.
The idea of the algorithm is to try to get to the final destination by prioritizing the possibilities closer to the destination, leaving all the others aside. So first, it will go to the most direct paths: if these paths do not allow to reach the final solution, it will examine the other solutions put aside.

**2. Parameters**

* **Open list**: The open list contains all nodes in the path that are neighbors to the current node being verified. These nodes have not yet been analyzed.
* **Closed list**: The closed list contains all the nodes in the grid that were already verified. They won't be analyzed again.
* **G cost**: It is the Euclidean distance between the starting point and the current node
* **H cost**: It is the Euclidean distance between the goal and the current node
* **F cost**: It is the sum of costs G and H
* **Weight parameter**: It is an optimization parameter. The higher its value, the more importance we give to the heuristic, and the faster our algorithm will be. On the other hand, when providing a very high value for the weight, we can lose the ideal path because we will not consider all possible solutions. After all, when choosing the path, the importance of heuristics will be predominant.

**3. Graphical interface**

To facilitate visualization of the problem, the solution also includes a graphical interface with elements in different colors:
* **Yellow**: Start and endpoints
* **White**: the free nodes to be taken
* **Black**: Obstacles
* **Green**: Open list nodes
* **Red**: Closed list nodes
* **Blue**: Final path
