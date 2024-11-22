from unittest.mock import MagicMock
import pytest
from liste_de_taches import ListeDeTaches

# Test de l'ajout d'une tâche
def test_ajouter_tache():
    liste = ListeDeTaches()
    liste.ajouter_tache("Faire les courses")
    assert len(liste.taches) == 1
    assert liste.taches[0]["tache"] == "Faire les courses"
    assert liste.taches[0]["terminee"] is False

# Test de la suppression d'une tâche
def test_supprimer_tache():
    liste = ListeDeTaches()
    liste.ajouter_tache("Faire les courses")
    liste.supprimer_tache("Faire les courses")
    assert len(liste.taches) == 0

# Test de marquage d'une tâche comme terminée
def test_marquer_terminee():
    liste = ListeDeTaches()
    liste.ajouter_tache("Faire les courses")
    liste.marquer_terminee("Faire les courses")
    assert liste.taches[0]["terminee"] is True

# Test pour obtenir les tâches incompletes
def test_obtenir_taches_incompletes():
    liste = ListeDeTaches()
    liste.ajouter_tache("Faire les courses")
    liste.ajouter_tache("Lire un livre")
    liste.marquer_terminee("Faire les courses")
    incompletes = liste.obtenir_taches_incompletes()
    assert "Lire un livre" in incompletes
    assert "Faire les courses" not in incompletes

