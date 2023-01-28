#importer datetime pour la date de circulation
from datetime import datetime
class Voiture :
    def __init__(self, marque='', matricule='', dat_circ=datetime.now(), kilometrage='', cylindre='') :
        self.marque = marque 
        self.matricule = matricule
        self.dat_circ = dat_circ
        self.kilometrage = kilometrage
        self.cylindre = cylindre

    def affiche(self) :
        print((" {0:<8} | {1:<9} | {2:<15s} |  {3:<8}| {4:<10} ").format(self.marque,self.matricule,self.dat_circ.strftime('%d-%m-%Y'),self.kilometrage,self.cylindre))    #saisir les données d'une voiture
    def saisie(self) :
        self.marque = input("Marque :")
        self.matricule = input("matricule :")
        self.dat_circ = input("dat_circulation :")
        self.dat_circ = datetime.strptime(self.dat_circ, '%Y-%m-%d')
        self.kilometrage = input("kilometrage :")
        self.cylindre = int(input("cylindre :"))
    
    
    # def __str__(self) :
    #     return "Marque :%s  matricule :%s  date_circulation : %s  kilometrage :%d  cylindre :%d" % (self.marque, self.matricule, self.dat_circ, self.kilometrage, self.cylindre)        
if __name__=='__main__' :
    v1 = Voiture()
    v1.saisie()
    v1.affiche()