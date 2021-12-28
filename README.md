# Directed Weighted Graph - Python
**Created by Eldad Tsemach, Ilan Sirisky and Nir Meir**
 
- [Link to Wiki page](https://github.com/TorNim0s/Directed-Weighted-Graph-Python/wiki)

# Table of Contents
1. [About the Project](#About)
2. [Algorithms](#algorithms)
3. [Code Description](#code)
4. [Dependencies](#dependencies)
5. [How to Run](#run)
6. [Examples](#examples)
7. [Matplot Graph](#matplot)
8. [UML](#uml)

## About the Project <a name="About"></a>
This is task  3 in our OOP course.

It is based on task 2 about Directed Weighted Graphs.

This time we were asked to implement the algorithms in Python.

## List of algorithms <a name="algorithms"></a>
1. Checking if a DW graph is strongly connected by using the DFS algorithm.

2. Finding the shortest path between source and destination nodes by using Dijkstra algorithm.

3. Finding the center of a DW graph which minimizes the max distance to all the other nodes.
4. Computing a list of consecutive nodes which go over a list of nodes and finding the least costing path between all the nodes,
        similar to the Traveling Salesman Problem but without the limitaion of visiting each node only once.
5. Saving and loading a graph to and from a .json file which contains an array of Edges and Nodes.

The dijkstra algorithm finds the shortest path between two nodes in a DW graph.
For further reading see: https://en.wikipedia.org/wiki/Dijkstras_algorithm.

Example of the algorithm:

![gif](https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Dijkstra_Animation.gif/220px-Dijkstra_Animation.gif)


## Code Description <a name="code"></a>
- `Node.py` : Implements and represents the vertices of the graph.
- `Edge.py`: Implements and represents the edges of the graph.
- `DiGraph.py`: Implements the graph itself, by using 2 hashmaps one for NodeData and the other for EdgeData.
- `GraphAlgo.py`: Implements all the algorithms that are listed above.


## Dependencies <a name="dependencies"></a>
This project is using Python version `3.9`.

We are using Matplotlib in order showcase the graph.

# How to Run <a name="run"></a>
To run this project, download the files from the github.

Inside the project you can find `main.py`, there you run the any algorithm that you want.

There are 4 checks that are ready that you can run.

Feel free to change/add more tests as you wish. 

## Input/Output Examples <a name="examples"></a>
### Example for A1.json input :
![Building](https://i.imgur.com/Xl0jAQl.png)| ![](https://i.imgur.com/xZjCTM0.png)
##### In Edges :
- *src* : the ID of the source node.
- *w* : the weight of the edge.
- *dest* : the ID of the destination node.

##### In Nodes :
- *pos* : containing the GeoLocation of the node based on x,y,z.
- *id* : the ID of the node.

### Graph A1.json in Matplotlib : <a name="matplot"></a>
![](https://i.imgur.com/QTyCCNi.png)

## UML <a name="uml"></a>
![](https://i.imgur.com/DjIYCVr.png)

Link to the main assignment: https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex3.
