from BancoDelas_Cliente import Cliente

class ContaCorrente(Cliente):
    def __init__(self):
        super().__init__()
        self.__saldo = 0.0

    @property
    def saldo(self):
        return self.__saldo #valor do saldo

    def depositar(self):
        valor = float(input('Digite um valor [ex.: 1.590,59]: ').replace('.', '').replace(',', '.'))
        while True:
            if not valor:
                print("O sexo não pode ser em branco!")
                continue
            if valor < 0:
                print("O valor do depósito deve ser positivo!")
                continue
            else:
                self.__saldo += valor
                print(f'\nDepósito de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {self.__saldo:.2f}')
                break
                        
    
    def sacar(self):
        if self.__valor <= 0:
            print("O self.__valor do saque deve ser positivo!")
            return
        
        if self.__valor > (self.__saldo + self.cheque_especial):
            while True:
                print(f'Não é possível realizar o saque, seu saldo é R${self.__saldo:.2f}, insuficiente para realizar o saque do valor de R${self.__valor:.2f}!')
                escolha = input('Deseja sacar novo valor? [S/N]  ').strip().lower()
                
                if escolha in ['s', 'sim']:
                    novo_valor = input('Digite o novo valor: ')
                    self.__valor = float(novo_valor.replace('.', '').replace(',', '.'))
                    
                    if self.__valor <= 0:
                        print("O valor do saque deve ser positivo!")
                        continue
                    
                    if self.__valor <= (self.__saldo + self.cheque_especial):
                        break
                else:
                    print('Operação cancelada.')
                    return
        
        # If we're here, self.__valor is within the limit.
        if self.__valor <= self.__saldo:
            self.__saldo -= self.__valor
        else:
            cheque_utilizado = self.__valor - self.__saldo
            self.__saldo = 0
            self.cheque_especial -= cheque_utilizado

        print(f'Saque de R${self.__valor:.2f} realizado com sucesso! Saldo atual: R${self.__saldo:.2f}')

    def __str__(self):
        return (f'Saldo atual: R$ {self.__saldo:.2f}\n'
                f'Cheque Especial disponível: R$ {self.cheque_especial:.2f}')


    # def sacar(self, valor):
    #     if valor <= 0:
    #         print("O valor do saque deve ser positivo!")
    #     elif valor > (self.__saldo + self.cheque_especial):
    #         while True:                               
    #             print(f'Não é possível realizar o saque, seu saldo é R${self.__saldo:.2f}, insuficiente para realizar o saque do valor de R${valor:.2f}!')
    #             escolha = str(input('Deseja sacar novo valor? [S/N]  '))
    #             if escolha.lower() == 's':
    #                 novo_valor = input('Digite o novo valor: ')
    #                 valor = float(novo_valor.replace('.', '').replace(',', '.'))
                   
    #                 if self.sexo.lower() == 'masculino':
    #                     print(f'Não é possível realizar o saque, seu saldo é R${self.__saldo:.2f}, insuficiente para realizar o saque do valor de R${valor:.2f}!')
                       
    #                     if self.renda_mensal <= self.__saldo :
    #                         novo_valor = valor - self.__saldo 
    #                         print('Valor sacado com sucesso!') 
    #                         break
                    
    #                 print('Valor sacado com sucesso!') 
    #                 float(valor) = self.__saldo - novo_valor
    #                 # novo_valor = valor - self.__saldo #<--
    #                 # self.cheque_especial -= novo_valor #<-- tirar essa linha caso nao passe da validacao acima
    #                 # self.__saldo = neg(novo_valor) #<-- para caso tenha cheque especial e tirar dele e deixar negativa o saldo
                    
    #                 print(f'Saque de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {self.__saldo:.2f}')
    #                 break

    #             print('Operação cancelada') 
    #             break  
    #     else:
    #         if valor <= self.__saldo:
    #             self.__saldo -= valor
    #         else:
    #             cheque_utilizado = valor - self.__saldo
    #             self.cheque_especial -= cheque_utilizado
    #             self.__saldo = neg(cheque_utilizado)
                    
    #         print(f'Saque de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {self.__saldo:.2f}')
    
    def __str__(self):
        return (super().__str__() +
                f'\nSaldo atual: R$ {self.saldo:.2f}') #faz a adição do print do saldo junto com os demais dados acima na classe conta corrente
