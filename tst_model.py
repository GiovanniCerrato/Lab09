from model.model import Model

m = Model()
m.buildGraph(770)
print(m._graph.edges(data=True))
