from time import time
from random import seed, random

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,mensage):
        self.mensage = mensage


FACIL   = 0.5
NORMAL  = 1
DIFICIL = 1.5

def apresentacao():
    print('***********************')
    print('* Jogo da Adivinhação *')
    print('***********************')
    return 0

def escolhe_grau_do_jogo():
    while True:

        try:
            grau = int(input('Escolha (1)Fácil | (2)Normal | (3)Difícil '))

            if grau > 3:
                raise InputError('Escolha somente os numeros 1, 2 ou 3')

            if grau == 1:
                return FACIL
            
            if grau == 2:
                return NORMAL

            if grau == 3:
                return DIFICIL
        except ValueError:
            print('Escolha somente números um  1, 2 ou 3')
        except InputError as ex:
            print(ex)


def escolhe_numero_secreto():
    
    anything = time()
    seed(anything)
    
    return int(random()*100)


def teste_igualdade(palpite,numero_secreto):
    if palpite == numero_secreto:
        return True

def testa_diferenca(palpite,numero_secreto,dificuldade):
    if palpite > numero_secreto:
        print('Seu palpite é maior que o número secreto\n')
    else:
        print('Seu palpite é menor que o número secreto\n')
    
    return abs(numero_secreto-palpite) * dificuldade

#Inicio do jogo!

if __name__ == "__main__":
    total_de_pontos = 1000

    numero_secreto = escolhe_numero_secreto()


    apresentacao()

    dificuldade = escolhe_grau_do_jogo()

    while True:
        
        palpite = int(input('Qual é o seu palpite para o numero secreto? '))

        if teste_igualdade(palpite,numero_secreto):
            break
        
        total_de_pontos -= testa_diferenca(palpite,numero_secreto,dificuldade)

    print('Parabéns você acertou o número secreto')
    print(total_de_pontos)
