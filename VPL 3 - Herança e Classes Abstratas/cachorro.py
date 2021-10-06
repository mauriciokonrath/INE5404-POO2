from mamifero import Mamifero

class Cachorro(Mamifero):
    def __init__(self, volumeSom=3, tamanhoPasso=3):
        super().__init__(volumeSom, tamanhoPasso)

    def produzirSom(self):
        return 'MAMIFERO: PRODUZ SOM: ' + str(self.tamanhoPasso) + ' SOM: AU'
       
        
    def latir(self):
        return self.produzirSom()