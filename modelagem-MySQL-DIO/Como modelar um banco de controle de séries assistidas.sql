/*

    Projeto: MySql - Como modelar um banco de controle de séries assistidas
    Autor:   José Francisco Azevedo da Silva
    Data:    29/03/2022
    
*/

-- Criando o Banco de Dados 
create database if not exists movies_controll
DEFAULT CHARACTER SET utf8;

-- Selecionando o bancoo de dados "movies_controll"
use movies_controll;

-- Criando a tabela movies
create table movies(
	id int not null auto_increment primary key,
    type_of smallint not null,               
    name_of varchar(30) not null,         
    total_ep int,
    atual_ep int,
    last_view datetime default current_timestamp()
);

-- Type no workbench está sendo apresentada como uma palavra reservada modificado para "type_of como será usada somente 0 ou 1 foi atribuido como smalint" 
-- name no workbench está sendo apresentada como uma palavra reservada modificado para "name_of"
-- last_view para receber um default timestamp ser uma coluna datetime

-- inserindo dados na tabela movies

insert into movies(type_of, name_of, total_ep, atual_ep)
values(0, 'The man in the high castle', 30, 14);

insert into movies(type_of, name_of, last_view)
values (1, 'Matrix Resurrections', '2022-03-07 10:23:00');

-- modificar data do registro de ID 1 para o dia 18/02/2022
update movies set last_view = '2022-02-18'
where id = 1;

-- inserindo mais filmes
insert into movies(type_of, name_of, total_ep, atual_ep)
values(0, 'Fear the walking dead', 40, 35);

insert into movies(type_of, name_of, last_view)
values (1, '2012', '2012-07-20 14:00:00');

insert into movies(type_of, name_of, last_view)
values (1, 'Não olhe para cima', '2022-01-31 14:00:00');

-- Deletando um filme
delete from movies where id = 4;

select * from movies;

