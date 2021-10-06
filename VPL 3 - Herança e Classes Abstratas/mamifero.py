from abc import ABC, abstractmethod
from animal import Animal


class Mamifero(Animal, ABC):
    def __init__(self, volumeSom: int, tamanhoPasso: int):
        super().__init__(tamanhoPasso)
        self.__volumeSom = volumeSom

    @property
    def volumeSom(self):
        return self.__volumeSom

    @volumeSom.setter
    def volumeSom(self, volumeSom):
        self.__volumeSom = volumeSom

    @abstractmethod
    def produzirSom(self):
        pass