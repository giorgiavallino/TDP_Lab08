import flet as ft
from model.nerc import Nerc

class Controller:

    def __init__(self, view, model):
        # The view, with the graphical elements of the UI
        self._view = view
        # The model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap = {}
        self.fillIDMap()

    def handleWorstCase(self, e):
        # TO FILL
        pass

    def fillDDNerc(self):
        nercList = self._model.listNerc
        if nercList == []:
            print("C'è stato un problema nell'inizializzazione del dropdown.")
            return
        for nerc in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(nerc))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v