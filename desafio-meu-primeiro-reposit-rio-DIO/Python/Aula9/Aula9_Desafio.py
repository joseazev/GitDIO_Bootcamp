def registra_em_arquivo(texto):
    arquivo = open('lista_de_alunos.txt','a')
    arquivo.write(texto)
    arquivo.write('\n')
    arquivo.close

def verifica_aprovacao(media):
    if media >= 7:
        return {'Situação': 'Aprovado'}
    else:
        return {'Situação': 'Reprovado'}

def ler_notas(arquivo):
   arquivo = open(arquivo,'r')
   alunos_notas = arquivo.read()
   alunos_notas = alunos_notas.split('\n')
   arquivo.close
   return alunos_notas

def monta_dicionario(notas,media,situacao):
    notas = { 'notas' : notas} 
    media = {'media': media}
    notas.update(media)
    notas.update(situacao)
    return notas

def calcula_media(lista):
    for x in lista:
        lista_nota = x.split(',')
        aluno = lista_nota[0]
        lista_nota.pop(0)
        
        notas = lambda notas : [float(i) for i in notas]
        media = lambda notas : sum([float(i) for i in notas]) / 4
        notas = notas(lista_nota)
        media = round(media(lista_nota),2)
        
        situacao = verifica_aprovacao(media)
        
        aprovacao = monta_dicionario(notas,media,situacao)

        registra_em_arquivo(aluno)
        registra_em_arquivo(str(aprovacao))

        print(aluno)
        print(aprovacao)


if __name__ == '__main__':
    lista = ler_notas('notas.txt')
    calcula_media(lista)
