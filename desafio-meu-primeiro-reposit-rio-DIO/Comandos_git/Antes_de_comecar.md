# Introdução ao git e ao Github

## Porque dominar esses comandos?

É uma tecnologia que hoje é um padrão de mercado que cuida de versionamento de software.

_Onde o git github pode ajudar?_

1. Controle de Versão

2. Armazenamento em nuvem

3. Trabalho em equipe

4. Melhoria do código

5. Reconhecimento

## Antes de começar

#### Vamos ver uns comandos básicos para um bom desempenho

| Comandos         | Windows | Linux  |
|:---------------- |:-------:| ------:|
| Listar diretório | dir     | ls     |
| Limpar terminal  | cd      | cd     |
| Deletar arquivos | cls     | clear  |
| Criar pasta      | mkdir   | mkdir  |
| Deletar pasta    | rmdir   | rm -rf |

## Entendendo como o git funciona.

Para controle dos arquivos o git utiliza o sha*, que cria uma hash(código) que quando algo no arquivo é modificado a Hash não se repete.

_SHA - é uma tecnologia de encriptação, é muito bem sucecida pois gera hash de 40 caracteres de forma rápida_

|         | Objetos internos do Git                                                                                                                                                          |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Blos    | Insere metadados com informações do arquivo que será encriptado.                                                                                                                 |
| Trees   | A arvore será responsável por apontar outras arvores(quando houver) e terá informações de diretório e mais informações nome do aqruivo  além do blobs                            |
| Commits | É o que vai  abranger  tudo,  apontar  para  outros  commits,  apontar  para  arvores,  apontar  para  o autor,  apontar  para  a  mensagem  e  esse  objeto  tem  um timestamp. |

O fato do git ser um sistema com encriptação e ser distribuído, faz com que todos cópias do código sejam muito confiáveis.
