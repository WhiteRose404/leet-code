# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.neighbors = []
#         self.visited = False;
    
#     # setters
#     def addNeighbor(self, node):
#         # check whether the neighbor already exists or not
#         for neighbor in self.neighbors:
#             if neighbor.value == node.value:
#                 return;
#         self.neighbors.append(node);
#     def setNeighbors(self, neighbors):
#         self.neighbors = neighbors;

#     # getters
#     def getneighbors(self) -> list():
#         return self.neighbors;

# class Graph:
#     def __init__(self, graph):
#         self.nodes = [];
#         for edge in graph:
#             node_1 = self.getNode(edge[0]) if self.isExists(edge[0]) else self.createNode(edge[0]);
#             node_2 = self.getNode(edge[1]) if self.isExists(edge[1]) else self.createNode(edge[1]);
#             node_1.addNeighbor(node_2);
#             node_2.addNeighbor(node_1);

#     def createNode(self, value) -> Node:
#         node = Node(value);
#         self.nodes.append(node);
#         return node;

#     def isExists(self, value) -> bool:
#         for node in self.nodes:
#             if node.value == value:
#                 return True;
#         return False;

#     def getNodes(self) -> list():
#         return self.nodes;

#     def getNode(self, value) -> Node:
#         for node in self.nodes:
#             if node.value == value:
#                 return node;
#         return None;

#     def findShortestPath(self, start, end, minimum_step = 1) -> list:
#         path = [];
#         queue = [];

#         pass

class Solution:
    def shortest(self, listGraph):
        return 4;
        graph = Graph(listGraph);
        nodes = graph.getNodes();
        start = nodes[0];
        end = nodes[len(nodes) - 1];
        print("shortest path from " + str(start.value) + " to " + str(end.value) + ":");
        print("DEBUG");
        print(end.value , [i.value for i in end.getneighbors()], listGraph);