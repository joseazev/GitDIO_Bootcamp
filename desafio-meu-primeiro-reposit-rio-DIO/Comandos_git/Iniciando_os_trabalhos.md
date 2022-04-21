Nessa sessão vamos ver alguns comandos para iniciar os
trabalhos com Git.

#### Comando para iniciar o Git

- git init

#### Verificar o estágio de situação do arquivo com o Git

- git status

#### Configurar o git na maquina local

- git config --local user.name [seu nome]

- git config --local user.name [seu e-mail]

> Dica: A boa pratica indica que o email deve ser o mesmo do GitHub!

#### Salvar um arquivo no Git. _(Assim o git poderá monitoralo)_

- git add [Nome do arquivo]

> Dica: também poderá ser usado o caracter " . " ponto, assim todos os arquivos da pasta serão adicionados.

#### Enviar a modificações a serem salvas no git (commit)

- git commit -m "Mensagem"

#### Visualizar histórico

- git log

- git log --oneline (resumido)

- git log -p (tetalhado)

- git log --pretty="[Parametro de formatação](https://devhints.io/git-log)"

## Antes que eu me esqueça

Pode acontecer de ter arquivos no seu projeto que não precise ser guardado ou monitorados pelo git. paa o git ignorar pasta ou arquivo de seu projeto 

Crie um arquivo ".gitignore".

- Escreva o nome_da_pasta/ (Ex. novapasta/)

- Escreva o nome_do_arquivo (Ex. IDE-conf)

> Depois será necessário adicionar o arquivo gitignore
> 
> git add .gitignore
> 
> git commit -m "Adicionando o arquivo gitignore"
