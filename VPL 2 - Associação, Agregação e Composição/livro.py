from capitulo import Capitulo
from editora import Editora
from autor import Autor

class Livro:
    
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @property
    def autores(self):
        return self.__autores
    

    def incluirAutor(self, autor: Autor):
        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        if type(autor) is Autor:
            if autor in self.__autores:
                print()
            else:
                self.__autores.append(autor)
        
    def excluirAutor(self, autor: Autor):
        if autor in self.__autores:
            for i in range(len(self.__autores)):
                if self.__autores[i] == autor:
                    self.__autores.pop(i)
                    break
                
    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        capitu = 0
        for i in range(len(self.__capitulos)):
            if numeroCapitulo == self.__capitulos[i].numero:
                capitu = 1
        if capitu == 0:
            numCap = Capitulo(numeroCapitulo, tituloCapitulo)
            self.__capitulos.append(numCap)
        

    def excluirCapitulo(self, tituloCapitulo: str):
        for i in range(len(self.__capitulos)):
            if tituloCapitulo == self.__capitulos[i].titulo:
                self.__capitulos.pop(i)
                break

    def findCapituloByTitulo(self, tituloCapitulo: str):
        for i in range(len(self.__capitulos)):
            if tituloCapitulo == self.__capitulos[i].titulo:
                return self.__capitulos[i]
        