from collections import Sequence
from random import shuffle


class Tombola(Sequence):
    def __init__(self):
        self.itens = list()

    def __len__(self):
        return len(self.itens)

    def __getitem__(self, key):
        return list(reversed(self.itens))[key]

    def carregar(self, bolas):
        self.itens.extend(bolas)

    def sortear(self):
        return self.itens.pop()

    def carregada(self):
        return bool(self.itens)

    def misturar(self, embaralhador=shuffle):
        embaralhador(self.itens)
