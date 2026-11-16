
class Ressource:
    def __init__(self, nom: str):
        self.nom = nom
        print(f"[INIT] Création de la ressource '{nom}'")

    def __del__(self):
        """Appelé quand l'objet est détruit."""
        print(f"[DEL] Destruction de la ressource '{self.nom}'")

    def utiliser(self):
        print(f"[USE] Utilisation de '{self.nom}'")


# Test
import gc

# Création de l'objet
r = Ressource("Fichier de données")
r.utiliser()

# Suppression explicite
del r

# Forçage du garbage collector
gc.collect()
