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
    
class Cliente(Banco):
    def __init__(self):
        super().__init__()
        self._sexo = None
        self._cheque_especial = 0
    
    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self, value):
        while True:
            if not isinstance(value, str):
                print("O sexo deve ser uma string!")
                continue
            if not value:
                print("O sexo não pode ser em branco!")
                continue
            self._sexo = value
            break

    @property
    def cheque_especial(self):
        return self._cheque_especial

    @cheque_especial.setter
    def cheque_especial(self, value):
        self._cheque_especial = value #adicionando '0' no choque ou valor da renda, caso seja feminino o genero

    def alterar_nome(self):
        novo_nome = input('Digite o nome da conta: ').capitalize()
        self.nome = novo_nome #inserindo novo nome
        
    def alterar_telefone(self):
        novo_telefone = input('Digite o seu telefone: ')
        self.telefone = novo_telefone #inserindo novo telefone
    
    def alterar_sexo(self):
        while True:
            sexo = input('Digite o seu sexo(F|M): ')
            if sexo.lower() == 'f': 
                self.sexo = 'Feminino' #inserindo a str 'feminino'
                self.cheque_especial = self.renda_mensal
                break
            elif sexo.lower() == 'm':
                self.sexo = 'Masculino' #inserindo a str 'masculino'
                self.cheque_especial = 0 #inserindo zerado o cheque por ser genero masculino
                break
            else:
                print("Sexo inválido! Use 'f' para feminino ou 'm' para masculino.")
        
    def alterar_renda_mensal(self):
        nova_renda_mensal = float(input('Digite sua renda mensal: ').replace('.', '').replace(',', '.'))
        self.renda_mensal = nova_renda_mensal #inserindo nova renda mensal

    def __str__(self): #esse def str vem do super do conta corrente
        return (f'Seus dados: \n'
                f'Nome: {self.nome} \n'
                f'Telefone: {self.telefone} \n'
                f'Sexo: {self.sexo} \n'
                f'Renda Mensal: {self.renda_mensal} \n'
                f'Cheque especial disponível: {self.cheque_especial}')
    
class ContaCorrente(Cliente):
    def __init__(self):
        super().__init__()
        self.__saldo = 0.0

    @property
    def saldo(self):
        return self.__saldo #valor do saldo

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo!")
        else:
            self.__saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {self.__saldo:.2f}')
                        
    
    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo!")
        elif valor > (self.__saldo + self.cheque_especial):
            while True:                               
                print(f'Não é possível realizar o saque, seu saldo é R${self.__saldo:.2f}, insuficiente para realizar o saque do valor de R${valor:.2f}!')
                escolha = str(input('Deseja sacar novo valor? [S/N]  '))
                if escolha.lower() == 's':
                    novo_valor = input('Digite o novo valor: ')
                    valor = float(novo_valor.replace('.', '').replace(',', '.'))
                   
                    if self.sexo.lower() == 'masculino':
                        print(f'Não é possível realizar o saque, seu saldo é R${self.__saldo:.2f}, insuficiente para realizar o saque do valor de R${valor:.2f}!')
                       
                        if self.renda_mensal <= self.__saldo :
                            novo_valor = valor - self.__saldo 
                            print('Valor sacado com sucesso!') 
                            break
                    
                    print('Valor sacado com sucesso!') 
                    float(valor) = self.__saldo - novo_valor
                    # novo_valor = valor - self.__saldo #<--
                    # self.cheque_especial -= novo_valor #<-- tirar essa linha caso nao passe da validacao acima
                    # self.__saldo = neg(novo_valor) #<-- para caso tenha cheque especial e tirar dele e deixar negativa o saldo
                    
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {self.__saldo:.2f}')
                    break

                print('Operação cancelada') 
                break  
        else:
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                cheque_utilizado = valor - self.__saldo
                self.cheque_especial -= cheque_utilizado
                self.__saldo = neg(cheque_utilizado)
                    
            print(f'Saque de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {self.__saldo:.2f}')
    
    def __str__(self):
        return (super().__str__() +
                f'\nSaldo atual: R$ {self.saldo:.2f}') #faz a adição do print do saldo junto com os demais dados acima na classe conta corrente

# Exemplo de uso:
conta_corrente = ContaCorrente()
conta_corrente.alterar_nome()
conta_corrente.alterar_telefone()
conta_corrente.alterar_renda_mensal() #ex. 2000
conta_corrente.alterar_sexo()

print()
print(conta_corrente)
print()
# Realizando operações de depósito e saque
conta_corrente.depositar(1000.0)
# conta_corrente.sacar(1500.0)
conta_corrente.sacar(1500.0)  # Testando saque além do saldo disponível

print()
print(conta_corrente)
