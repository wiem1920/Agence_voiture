from Voiture import Voiture

class Agence:
    def __init__(self):
        self.voitures = []

    def add_voiture(self, voiture):
        self.voitures.append(voiture)

    def delete_voiture(self, voiture):
        self.voitures.remove(voiture)
    
    def show_voitures(self):
        for voiture in self.voitures:
            voiture.affiche()
            
    def recherche(self,matricule):
        for voiture in self.voitures:
            if voiture.matricule == matricule:
                print("la voiture existe")
                return True;
            else:
                print("la voiture n'existe pas")
                return False; 
    
                
    def tri_voiture_selon_date(self):
        self.voitures.sort(key=lambda x: x.dat_circ)
        self.show_voitures()
    
    def get_voiture_plus_recente_selon_date(self):
        self.tri_voiture_selon_date()
        return self.voitures[0]
    
    def get_voiture_plus_anciennne_selon_date(self):
        self.tri_voiture_selon_date()
        return self.voitures[-1]
    
    

if __name__ == '__main__':
    my_agence = Agence()
    car1 = Voiture()
    car1.saisie()
    my_agence.add_voiture(car1)
    #my_agence.recherche("183TUN3000")

    car2 = Voiture()
    car2.saisie()
    my_agence.add_voiture(car2)
    # car3 = Voiture()
    # car3.saisie()
    # my_agence.add_voiture(car3)
    # my_agence.show_voitures()
    my_agence.get_voiture_plus_anciennne_selon_date()
    # my_agence.get_voiture_plus_recente_selon_date()