class Error(Exception):
    pass

class inputError(Error):
    def __init__(self,mensage):
        self.mesage = mensage

def calcula_media():
    while True:
        try:
            a = round(float(input('Digite a primeira nota: ')),1)

            if a > 10 or a < 0:
                raise inputError('Entre com valores entre 0 e 10')
            break
        except inputError as ex:
            print(ex)
        except ValueError as ex:
            print('''Favor certificar que está digitando valores numericos
    Casas decimais devem ser separadas com "."(ponto)
                ''')

    while True:
        try:
            b = round(float(input('Digite a Segunda nota:  ')),1)

            if b > 10 or b < 0:
                raise inputError('Entre com valores entre 0 e 10')
        except inputError as ex:
            print(ex)

    #TODO: Complete os espaços em branco com as respectivas variáveis para o cálculo da média.
    media = ( a * 3.5 + b * 7.5) / 11

    #TODO: Complete com a variável que representa o resultado da média.
    print(f'MEDIA = { media: 2.5f}')

