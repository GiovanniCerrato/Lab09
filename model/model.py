import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._allVoli = None



    def buildGraph(self,distanzaMinima):
        self._graph.clear()
        self._possibiliEdges = DAO.getPossibiliEdges()
        for e in self._possibiliEdges:
            if e.distanzaMediaPercorsa >= distanzaMinima:
                self._graph.add_edge(e.a1 , e.a2, weight=e.distanzaMediaPercorsa)
        print(self._graph)
        return self._graph
