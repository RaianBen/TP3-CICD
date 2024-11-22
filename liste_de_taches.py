class ListeDeTaches:
    def __init__(self, email_service=None):
        self.taches = []
        self.email_service = email_service if email_service else EmailService()

    def ajouter_tache(self, tache, email=None):
        self.taches.append({"tache": tache, "terminee": False})
        if self.email_service and email:
            self.email_service.envoyer_email(email, f"Tâche '{tache}' ajoutée.")

    def supprimer_tache(self, tache):
        self.taches = [t for t in self.taches if t["tache"] != tache]

    def marquer_terminee(self, tache):
        for t in self.taches:
            if t["tache"] == tache:
                t["terminee"] = True
                break

    def obtenir_taches_incompletes(self):
        return [t["tache"] for t in self.taches if not t["terminee"]]
        
