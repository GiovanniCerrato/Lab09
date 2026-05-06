import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()




    #primo modo con query sql complicata e che non saprei formulare all'esame
    def buildGraph(self,distanzaMinima):
        self._graph.clear()
        self._possibiliEdges = DAO.getPossibiliEdges()
        for e in self._possibiliEdges:
            if e.distanzaMediaPercorsa >= distanzaMinima:
                self._graph.add_edge(e.a1 , e.a2, weight=e.distanzaMediaPercorsa)
        print(self._graph)
        return self._graph

    #secondo modo con query semplice ma python più tosto
    def buildGraph2(self, distanzaMinima):
        self._graph.clear()
        self._allVoli = DAO.getAllVoli()
        self._idMapTratte = {}
        self._idMapDistanze = {}

        for v in self._allVoli:
            key = tuple(sorted([v.ORIGIN_AIRPORT_ID, v.DESTINATION_AIRPORT_ID]))

            if key not in self._idMapTratte:
                self._idMapTratte[key] = (v.DISTANCE, 1)
            else:
                somma, count = self._idMapTratte[key]
                self._idMapTratte[key] = (somma + v.DISTANCE, count + 1)

        # media
        for key, (somma, count) in self._idMapTratte.items():
            self._idMapDistanze[key] = round(somma / count, 2)

        # costruzione grafo
        for key, distanza in self._idMapDistanze.items():
            if distanza >= distanzaMinima:
                self._graph.add_edge(key[0], key[1], weight=distanza)

        print(self._graph)
        return self._graph

    def getNumNodes(self):
        return self._graph.number_of_nodes()
    def getNumEdges(self):
        return self._graph.number_of_edges()
