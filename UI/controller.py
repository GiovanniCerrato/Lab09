import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_AnalizzaAereoporti(self, e):
        distanzaMinima = self._view.txt_distanzaMinima.value
        self._view.txt_result.clean()
        if distanzaMinima is None or distanzaMinima == "":
            self._view.create_alert("Inserire una distanza")
            self._view.update_page()
            return
        try:
            distanzaMinima = float(distanzaMinima)
        except ValueError:
            self._view.create_alert("Inserire un valore numerico!")
            self._view.update_page()
            return
        res = self._model.buildGraph2(distanzaMinima)

        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato contiene {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} archi"))
        if self._model.getNumNodes() == 0:
            pass
        else:
            self._view.txt_result.controls.append(ft.Text(f"Elenco di tutti gli archi con relativa distanza:"))
            for u, v, d in sorted(self._model._graph.edges(data=True), key=lambda x: (x[0], x[1])):
                self._view.txt_result.controls.append(ft.Text(f"({u} <-> {v});  Distanza: {round(d["weight"],2)}"))

        self._view.update_page()
        return