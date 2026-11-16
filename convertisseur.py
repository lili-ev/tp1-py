
class Convertisseur:
    # Attribut de classe
    taux_eur_dh = 10.9

    @staticmethod
    def vers_dh(euros: float) -> float:
        """Convertit des euros en dirhams."""
        return euros * Convertisseur.taux_eur_dh

    @classmethod
    def changer_taux(cls, nouveau_taux: float):
        """Modifie le taux de change."""
        if nouveau_taux <= 0:
            raise ValueError("Le taux doit être positif.")
        cls.taux_eur_dh = nouveau_taux

    @classmethod
    def depuis_dh(cls, dirhams: float) -> float:
        """Convertit des dirhams en euros."""
        return dirhams / cls.taux_eur_dh


# Test
print(Convertisseur.vers_dh(100))

Convertisseur.changer_taux(11.0)

print(Convertisseur.depuis_dh(110))

conv = Convertisseur()
print(conv.vers_dh(50))
