import math;

class Leaf:
    def __init__(self, key, value, history = []) -> None:
        self.key = key;
        self.value = value;
        self.history = history;
        self.children = [];
    def getValue(self) -> int:
        return self.value;
    def getKey(self) -> int:
        return self.key;
    def getHistory(self) -> list:
        return self.history;
    def isVisted(self) -> bool:
        return self.value in self.history;
    def addChild(self, child) -> None:
        self.children.append(child);

class Tree:
    def __init__(self, graph) -> None:
        self.graph = graph;
        self.shortest = math.inf;
        self.path = [];
    def fillTree(self, pivote) -> None:
        if(pivote.isVisted()):
            hist = pivote.getHistory();
            leng_hist = len(hist);
            if(leng_hist < self.shortest):
                self.shortest = leng_hist;
                self.path = hist + [pivote.getValue()];
            return None;
        for edge in self.graph:
            if(pivote.getKey() != edge[0] and pivote.getValue() == edge[1]):
                child = Leaf(pivote.getValue(), edge[0], pivote.getHistory() + [pivote.getKey()]);
                pivote.addChild(child);
                self.fillTree(child);
            
            elif(pivote.getKey() != edge[1] and pivote.getValue() == edge[0]):
                child = Leaf(pivote.getValue(), edge[1], pivote.getHistory() + [pivote.getKey()]);
                pivote.addChild(child);
                self.fillTree(child);
        return None;

    def getShortestCycle(self) -> int:
        return self.shortest;

    def getPath(self) -> list:
        return self.path;




class Solution:
    def extractNodes(self) -> set:
        nodes = set();
        for edge in self.graph:
            nodes.add(edge[0]);
            nodes.add(edge[1]);
        return nodes;

    def getEdge(self, node):
        for edge in self.graph:
            if(node in edge):
                return edge;

    def shortest(self, listGraph) -> int:
        self.graph = listGraph;
        nodes = self.extractNodes();
        shortest = math.inf;
        for node in nodes:
            v1, v2 = self.getEdge(node); 
            pivote = Leaf(node, v2 if node == v1 else v1);
            tree = Tree(listGraph);
            tree.fillTree(pivote);
            shcycle = tree.getShortestCycle();
            if(shcycle < shortest):
                shortest = shcycle;
        return -1 if shortest == math.inf else shortest + 1;