from BancoDelas import Banco


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
        self._cheque_especial = value #adicionando '0' no choque ou valor da renda, caso seja feminino o gênero

    def alterar_nome(self):
        novo_nome = input('Digite o nome da conta: ').capitalize()
        self.nome = novo_nome #inserindo novo nome
        
    def alterar_telefone(self):
        novo_telefone = input('Digite o seu telefone: ')
        self.telefone = novo_telefone #inserindo novo telefone
    
    def alterar_sexo(self):
        while True:
            sexo = input('Digite o seu sexo(F|M): ')
            if sexo.lower() in ['f', 'feminino']: 
                self.sexo = 'Feminino' #inserindo a str 'feminino'
                self.cheque_especial = self.renda_mensal
                break
            elif sexo.lower() in ['m', 'masculino']:
                self.sexo = 'Masculino' #inserindo a str 'masculino'
                self.cheque_especial = 0 #inserindo zerado o cheque por ser gênero masculino
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
    
