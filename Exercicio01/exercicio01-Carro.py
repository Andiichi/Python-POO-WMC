'''
1. Crie uma classe que modele o objeto "carro".
2. Um carro tem os seguintes atributos: ligado, cor, modelo,
velocidade.
3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
desacelera.
4. Crie uma instância da classe carro.
5. Faça o carro "andar" utilizando os métodos da sua classe.
6. Faça o carro "parar" utilizando os métodos da sua classe.

'''


#criação da classe objeto 'carro'
class Carro:
    #aatributos iniciais
    def __init__(self):
        self.ligado = 'desligado'
        self.cor = 'Red'
        self.modelo = 'Fusca'
        self.velocidade = 0
        self.velocidade_min = 0
        self.velocidade_max = 100

    def ligar(self):
        self.ligado = 'ligado'
    
    def desligar(self):
        self.ligado = 'desligado'

    def acelerar(self):
        if not self.ligado:
            return 
        
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10

    
    def desacelerar(self):
        if not self.ligado:
            return 
        
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10
        

    def __str__(self) -> str:
            return f'O carro está {self.ligado}\nVelocidade atual: {self.velocidade} Km/h'
        


# Crie uma instância da classe carro.

carro_mateus = Carro()
carro_andrezza = Carro()

#ligando o carro do mateus
carro_mateus.ligar()


# Faça o carro "andar" utilizando os métodos da sua classe.
for _ in range(2):
    carro_mateus.acelerar()

print('Carro do Mateus \n',carro_mateus)
print()


# Faça o carro "parar" utilizando os métodos da sua classe.

for _ in range(2):
    carro_mateus.desacelerar()

print('Carro do Mateus \n',carro_mateus)
print()

#estado do carro da andrezza
print()
print('Carro da Andrezza \n',carro_andrezza)