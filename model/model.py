from database.DAO import Dao

class Modello:

    def __init__(self):
        self._solBest = []
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()

    def worstCase(self, nerc, maxY, maxX):
        self._solBest = []
        self.loadEvents(nerc)
        for evento in self._listEvents:
            soluzione_parziale = [evento]
            eventi_rimanenti = self._listEvents.remove(evento)
            self.ricorsione(soluzione_parziale, eventi_rimanenti, maxY, maxX)
        return self._solBest

    def ricorsione(self, soluzione_parziale, eventi_rimanenti, maxY, maxX):
        if self.calcolaDurataAnni(soluzione_parziale) > maxX:
            print(soluzione_parziale)
        else:
            for evento in eventi_rimanenti:
                soluzione_parziale.append(evento)
                nuovi_eventi_rimanenti = eventi_rimanenti.remove(evento)
                self.ricorsione(soluzione_parziale, nuovi_eventi_rimanenti, maxY, maxX)
                soluzione_parziale.pop()

    def calcolaDurataAnni(self, soluzione_parziale):
        pass

    def loadEvents(self, nerc):
        self._listEvents = Dao.getAllEvents(nerc)

    def loadNerc(self):
        self._listNerc = Dao.getAllNerc()

    @property
    def listNerc(self):
        return self._listNerc

if __name__=="__main__":
    m = Modello()
    m.worstCase("PJM", 100, 200)