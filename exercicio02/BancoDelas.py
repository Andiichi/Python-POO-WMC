'''
1. O banco Banco Delas é um banco moderno e eficiente, com
vantagens exclusivas para clientes mulheres.
Modele um sistema orientado a objetos para representar contas
correntes do Banco Delas seguindo os requisitos abaixo.
● Cada conta corrente pode ter um ou mais clientes como
titular.
● O banco controla apenas o nome, o telefone e a renda
mensal de cada cliente.
● A conta corrente apresenta um saldo e uma lista de
operações de saques e depósitos.
● Quando a cliente fizer um saque, diminuiremos o saldo da
conta corrente. Quando ela fizer um depósito,
aumentaremos o saldo.
● Clientes mulheres possuem em suas contas um cheque
especial de valor igual à sua renda mensal, ou seja, elas
podem sacar valores que deixam a sua conta com valor
negativo até renda_mensal.
● Clientes homens por enquanto não têm direito a cheque
especial.

Para modelar seu sistema, utilize obrigatoriamente os conceitos
"classe", "herança", "propriedades", "encapsulamento" e "classe
abstrata".

'''
from abc import ABC, abstractmethod
from operator import neg


class Banco(ABC):
    def __init__(self):
        self._nome = None
        self.__telefone = None
        self.__renda_mensal = None
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        while True:
            if not isinstance(value, str):
                print("O nome deve ser uma string!")
                continue
            if not value:
                print("O nome não pode ser em branco!")
                continue
            self._nome = value
            break
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, value):
        while True:
            if not isinstance(value, str):
                print("O telefone deve ser uma string!")
                continue
            if not value:
                print("O telefone não pode ser em branco!")
                continue
            self.__telefone = value
            break
    
    @property
    def renda_mensal(self):
        return self.__renda_mensal #Valor armazenado
    
    @renda_mensal.setter
    def renda_mensal(self, value):
        while True:
            if not isinstance(value, (int, float)):
                print("A renda mensal deve ser um número!")
                continue
            if not value:
                print("A renda mensal não pode ser em branco!")
                continue
            self.__renda_mensal = value
            break
    
    @abstractmethod
    def alterar_nome(self):
        pass

    @abstractmethod
    def alterar_telefone(self):
        pass

    @abstractmethod
    def alterar_renda_mensal(self):
        pass
    