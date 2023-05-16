#code to create a database

create database unes;

use unes;

create table contatos(
	email varchar(60) not null unique,
    assunto varchar(60) not null,
    descricao varchar(255)
    );

select * from contatos;