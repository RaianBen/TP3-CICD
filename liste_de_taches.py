class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append({"tache": tache, "terminee": False})
  

    def supprimer_tache(self, tache):
        self.taches = [t for t in self.taches if t["tache"] != tache]

    def marquer_terminee(self, tache):
        for t in self.taches:
            if t["tache"] == tache:
                t["terminee"] = True
                break

    def obtenir_taches_incompletes(self):
        return [t["tache"] for t in self.taches if not t["terminee"]]
