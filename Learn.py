class Personne:
    def __init__(self, nom, âge):
        self.nom = nom
        self.âge = âge

    def se_presenter(self):
        print(f"Bonjour je m'appelle {self.nom} et j'ai {self.âge} ans")

class

moi = Personne("Caren", 18)
moi.se_presenter()