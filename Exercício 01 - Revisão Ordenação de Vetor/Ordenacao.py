"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""
class Ordenacao:
    def __init__(self, array_para_ordenar:[]):
        self.__array_para_ordenar = array_para_ordenar

    def ordena(self):
        lista = self.__array_para_ordenar[:]
        self.__array_para_ordenar = []
        for i in range(len(lista)):
            menor = min(lista) #criando uma lista, colocando o menor sempre no final
            self.__array_para_ordenar.append(menor)
            lista.remove(menor)
        return self.__array_para_ordenar

    def toString(self):
        ordem = ''
        for i in range(len(self.__array_para_ordenar)):
            if i == len(self.__array_para_ordenar) - 1:
                ordem += str(self.__array_para_ordenar[i])
            else:
                ordem += str(self.__array_para_ordenar[i])+','
        return ordem

array = [5,4,3,2,1]
ordena1 = Ordenacao(array)
print(ordena1.toString())