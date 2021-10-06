from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self, volumeSom = 2, tamanhoPasso = 2):
        super().__init__(volumeSom, tamanhoPasso)

    def produzirSom(self):
        return 'MAMIFERO: PRODUZ SOM: '+str(self.volumeSom)+' SOM: MIAU'

    def miar(self):
        return self.produzirSom()