from abc import ABC, abstractmethod
from animal import Animal


class Ave(Animal, ABC):
    def __init__(self, tamanhoPasso: int, alturaVoo: int):
        super().__init__(tamanhoPasso)
        self.__alturaVoo = alturaVoo

    @property
    def alturaVoo(self):
        return self.__alturaVoo

    @alturaVoo.setter
    def alturaVoo(self, alturaVoo):
        self.__alturaVoo

    def mover(self):
	    return 'ANIMAL: DESLOCOU '+str(self.tamanhoPasso)+' VOANDO'

    @abstractmethod
    def produzirSom(self):
        pass