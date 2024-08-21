from BancoDelas_Cliente import Cliente
from BancoDelas_CC import ContaCorrente
import msvcrt

def digite_qualquer_tecla():
    tecla = msvcrt.getch()
    return tecla


def menu_conta(info_nome):
    print(f'Olá, {info_nome.capitalize()}! Escolha uma opção de operação na sua conta corrente ')
    print('''   
                1. Realizar um deposito.
                2. Realizar um saque.
                3. Realizar nova conta corrente
                0. Encerrar o programa.
          
        Para voltar ao "menu inicial" pressione 'ENTER'...
          ''')
    
    opcao = input('Digite uma opção: ')

    match opcao:

        case'1':
            print('~ Deposito em conta ~ ')
            # Realizando operações de depósito e saque
            cliente.depositar()
            digite_qualquer_tecla()
            print()
            menu_conta(info_nome)

        case'2':
            print('~ Saque em conta ~ ')
            # Testando saque além do saldo disponível
            cliente.sacar()
            digite_qualquer_tecla()
            print()
            menu_conta(info_nome)

        case'3':
            cadastro_cliente()

        case'0':
            print('\nObrigada por usar nosso banco, volte sempre!')
            exit()
        
    if opcao == b'\r':
        #caso seja outra tecla sem ser as case acima, volta pro menu inicial
        menu_inicial()


def cadastro_cliente():            
    
        cliente.alterar_nome()
        cliente.alterar_telefone()
        cliente.alterar_renda_mensal()
        cliente.alterar_sexo()

        print('\nCadastro feito com sucesso! \nDigite qualquer tecla para visualizar o cadastro\n')
        digite_qualquer_tecla()
        print(cliente)

def menu_inicial():

    print('\nBem-vindos ao Banco Delas! Seu banco, mulher!')
    print('\n~ Já é cliente? [Digite 1] Caso seja para fazer cadastro [Digite 2]: ')
    
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1: 
        info_nome = input('Informe seu nome: ')
        menu_conta(info_nome)  

    elif opcao == 2: 
        cadastro_cliente()
        print('\nPara fazer uma operação na conta, pressione qualquer tecla ou digite 0 para finalizar programa: ')
        opcao2 = digite_qualquer_tecla()
    
        if opcao2 == 0:
            print('Saindo do programa...')
            exit()

        menu_conta()

    print('Opção invalida, tente novamente!') 
    menu_inicial()



if __name__ == "__main__":
   #instanciando a classe
    cliente = ContaCorrente()
    
    #iniciando o programa
    menu_inicial()