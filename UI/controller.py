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
        res = self._model.buildGraph(distanzaMinima)

        self._view.txt_result.controls.append(ft.Text(f"{res}"))
        self._view.txt_result.controls.append(ft.Text(f"Elenco di tutti gli archi con relativa distanza:"))
        for arco in res.edges(data=True):
            self._view.txt_result.controls.append(ft.Text(f"({arco[0]}, {arco[1]}, Distanza: {arco[2]["weight"]}))"))

        self._view.update_page()
        return