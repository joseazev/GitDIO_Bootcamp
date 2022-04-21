#### Gerando repositório de somente leitura

- git init --bare

> Caso já tenha dado o init e esqueceu do bare.
> 
> git config core.bare true

#### Adicionar repositório remoto

- git remote [nome do repositório] add [local onde ficará]

#### Verificar se foi adicionado

- git remote

- git remote -v

## Sincronizando os dados

#### Enviando para repositório criado

- git push [local] "*master*" ou "*main*"

#### Trazer dados do repositório

- git pull local "*master*" ou "*main*"

#### Renomear repositório

- git remote [nome antigo] [novo nome]

> Modificar nome de repositório se for o local da sua empresa, caso for o repositório do GitHub, a boa pratica recomenda manter o nome origin.
> 
> Não seja o primeiro a quebrar uma tradição.



```
No dia a dia Antes de realizar o comando git push convém fazer o 
git pull para verificar se há conflito e está sempre na ultima versão.
```
