## Branches

> Todo software de gerenciamento de versões tem algum tipo de ramificações (Branch) , Branch são utilizadas para desenvolver funcionalidades isoladas.



#### Criar muma branch

- git branch [nome]



#### Para visualizar a branch

- git branch



#### Para troca de branch

- git checkout [nome_da_branch_destino]

> Atalho para criar e modificar a branch
> 
> git checkout -b [nome_da_branch] 



#### Unir os trabalhos de duas branch

*Recomendasse fazer esse processo na branch master*

1. git chechout master

2. git merge [nome da branch]

*Esse comando adiciona mais um commit de merge*



#### Adicinar o(s) commit(s) criado por outra branch e não adicionar um commit de merge.

- git rebase [nome da branch]



#### Visualizando os commits em paralelo de maneira mais interessante

- git log --graph




















