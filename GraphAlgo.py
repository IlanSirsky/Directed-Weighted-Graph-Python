import json
import random
import sys
from typing import List
import numpy as np
import matplotlib.pyplot as plt

from DiGraph import DiGraph
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph = DiGraph()):
        self._graph = graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, encoding='utf-8') as f:
                json_string = f.read()
            a = json.loads(json_string)
            new_g = DiGraph()
            if a.get('Nodes')[0].get('pos') is not None:
                for node in a.get('Nodes'):
                    pos = tuple([float(a) for a in node.get('pos').split(",")])
                    new_g.add_node(node.get('id'), pos)
            else:
                for node in a.get('Nodes'):
                    new_g.add_node(node.get('id'))
            for edge in a.get('Edges'):
                new_g.add_edge(edge.get('src'), edge.get('dest'), edge.get('w'))
            self._graph = new_g
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            json_nodes, json_edges = [], []
            for node in self._graph._nodes.values():
                x_val, y_val, z_val = node.getPos()
                node_dict = {'pos': '{x},{y},{z}'.format(x=x_val, y=y_val, z=z_val), 'id': node.getID()}
                json_nodes.append(node_dict)
            for source,dicts in self._graph._inedges.items():
                for weight,dst in dicts.items():
                    edge_dict = {'src':source, 'w': weight, 'dest': dst}
                    json_edges.append(edge_dict)
            json_dict = {'Edges': json_edges, 'Nodes': json_nodes}
            json_string = json.dumps(json_dict)
            with open(file_name, "w") as f:
                f.write(json_string)
            return True
        except Exception as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        prev, dist = self.DijkstraAlgo(id1)
        path = []
        nd = prev[id2]
        while (nd != None and prev[nd.getID()] != None):
            path.insert(0,nd.getID())
            nd = prev[nd.getID()]

        if nd != None:
            path.insert(0, nd.getID())

        path.append(id2)

        return((dist[id2], path))

    def DijkstraAlgo(self, src):
        visit = []
        dist = []
        prev = []
        for i in range(self._graph.v_size()):
            visit.append(i)
            dist.append(sys.maxsize)
            prev.append(None)
        dist[src] = 0

        while (visit):
            lowerIndex = 0
            lowerValue = dist[visit[lowerIndex]]
            for i in range(len(visit)):
                if(lowerValue > dist[visit[i]]):
                    lowerIndex = i
                    lowerValue = dist[visit[i]]
            edges = self._graph.all_out_edges_of_node(visit[lowerIndex])
            for dst, weight in edges.items():
                alt = dist[visit[lowerIndex]] + weight
                if(alt < dist[dst]):
                    dist[dst] = alt
                    prev[dst] = self._graph.getNode(visit[lowerIndex])

            visit.remove(visit[lowerIndex])

        return prev,dist

    def plot_graph(self) -> None:
        for src in self._graph.get_all_v().values():
            x,y = random.randint(5,25), random.randint(5,25)
            if src.getPos():
                x, y ,z = src.getPos()
            else:
                src.setPos((x,y))

            plt.plot(x,y, markersize=10, marker="o", color="blue")
            plt.text(x,y, str(src.getID()), color="red", fontsize=12)
            for dst in self._graph.all_out_edges_of_node(src.getID()).keys():

                x2, y2 = random.randint(5, 25), random.randint(5, 25)
                if self._graph.getNode(dst).getPos():
                    x2, y2, z2 = src.getPos()
                else:
                    self._graph.getNode(dst).setPos((x2, y2))

                x2, y2, z2 = self._graph.getNode(dst).getPos()
                plt.annotate("",xy=(x,y), xytext=(x2,y2), arrowprops=dict(arrowstyle="<-"))
        plt.show()


    def get_graph(self) -> GraphInterface:
        return self._graph

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        maxDis = sys.maxsize
        nodeKey = 0
        nodes = self._graph.get_all_v()
        for node in nodes.values():
            src = node.getID()
            maxShortPath = 0
            nodes2 = self._graph.get_all_v()
            for dst in nodes2.values():
                if(dst!=node):
                    checkPath = self.shortest_path(src,dst.getID())
                    dist = checkPath[0]
                    if(dist > maxShortPath):
                        maxShortPath = dist
            if(maxShortPath< maxDis):
                maxDis = maxShortPath
                nodeKey = src

        return (nodeKey, maxDis)
