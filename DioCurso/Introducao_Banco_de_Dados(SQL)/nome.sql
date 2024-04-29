DIO SQL
TIPOS DE DADOS
/* INRTEIRO(INTEGER)
	DECIMAL(DECIMAL/NUMERIC)
	CARACTER(CHARACTER/VARCCHAR)
	DATA/HORA(DATE/TYIME)
	BOOLEANO (BOOLEAN)
	TEXTI LONGO(TEXT)
	*/
	
	/* RESTRICOES DE VALOR
	   NOT NULL
	   UNIQUE
	   DEFAULT
	   CHAVES PRIMARIAS E ESTRANGEIRAS
	   AUTO INCREMENTO */
CREATE TABLE usuarios(
	ID INT,
	NOME VARCHAR(255) NOT NULL COMMENT 'NOME DO USUARIO',
	EMAIL VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-MAIL DO USUARIO',
	ENDERECO VARCHAR(50) NOT NULL COMMENT 'ENDERECO DO USUARIO',
	DATA_NASCIMENTO DATE NOT NULL COMMENT 'DATA DE NASCIMENTO DO USUARIO'
	   );
	   
CREATE TABLE DIO.destinos(
	id INT COMMENT 'ID DO DESTINO',
	NOME VARCHAR(255) NOT NULL UNIQUE COMMENT 'NOME DO DESTINO',
	DESCRICAO VARCHAR(255) NOT NULL COMMENT 'DESCRICAO DO DESTINO'
);

CREATE TABLE DIO.reservas(
	ID INT COMMENT 'IDENTIFICADOR UNICO DA RESERVA',
	ID_USUARIO INT COMMENT 'REFERENCIA AO ID DO USUARIO QUE FEZ A RESERVA',
	ID_DESTINO INT COMMENT 'REFERENCIA AO ID DO DESTINO DA RESERVA',
	DATA DATE COMMENT 'DATA DA RESERVA',
	STATUS VARCHAR(255) DEFAULT 'PENDENTE' COMMENT 'STATUS DA RESERVA(CONFIRMADA, PENDENTE, CANCELADA, ETC.)' 
	
);

insert into usuarios (ID,NOME, EMAIL, DATA_NASCIMENTO, ENDERECO) values (1,"jose breno", "teste@teste.com", "1992-10-05", "Av das rosas, 100 - Bairro alto araraquara/sp");

insert into destinos(id, nome, descricao) values (1, "Praia do rosa", "linda praia");

insert into reservas(id, ID_USUARIO, ID_DESTINO, STATUS, data) VALUE (1,1,1,"Pendente", "2023-11-11");

select * from usuarios
WHERE nome like "%breno%";

update usuarios
set id = 2
where EMAIL = "teste@teste.com";

insert into usuarios (ID,NOME, EMAIL, DATA_NASCIMENTO, ENDERECO) values (2,"Claudia Aguiar", "teste1@teste.com", "1998-12-12", "Av das rosas, 150 - Bairro alto araraquara/sp");

delete from usuarios
where id = 2;

/* alterando e excluindo tabelas*/

DROP TABLE 
ALTER TABLE 


create table usuarios_nova(
	id int,
	nome VARCHAR(255) not null comment 'nome do usuario',
	email VARCHAR(255) not null unique comment 'email do usuario',
	data_nascimento date not null comment 'data de nascimento',
	endereco varchar(100) not null comment 'endereco do usuario'
);


/* inserir linhas apartir de outra tabela (clone)*/

insert into usuarios_nova(id, nome, email, endereco, data_nascimento)
select id, nome, email, endereco, DATA_NASCIMENTO
from usuarios;

apagar tabela
drop table usuarios;

alterar tabela
alter table usuarios_nova rename usuarios;


alterar tamanho de coluna
alter table usuarios modify column ENDERECO varchar(150);


/*add chave primaria

create table nome_tabela(
	id primary key autoincrement,...


alter table nome da tabela modify column id int primary key

*/

/* chave estrangeira
create table nome_tabela(
	id int primary key,
	chave_estrageira int,
	FOREIGN (chave_estrageira) references {outra_tabela} (id);

*/

/* alterar tabela para colcar CHAVES

alter table (tabbela)
add CONSTRAINT (nome_constrant)
FOREIGN key(id)
references{outra_tabela} (id)