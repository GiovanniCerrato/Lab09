import time

from model.model import Model

m = Model()

tic = time.time()
m.buildGraph(0)
toc = time.time()
print(f"buildGraph took {toc - tic} s")
print(m._graph.edges(data=True))

tic = time.time()
m.buildGraph2(0)
toc = time.time()
print(f"buildGraph took {toc - tic} s")
for u, v, d in sorted(m._graph.edges(data=True), key=lambda x: x[0]):
    print(u, v, d)