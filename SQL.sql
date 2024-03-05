/* modelagem basica*/
ENTIDADE = TABELA
CAMPOS = ATRIBUTOS

/

CLIENTE 

NOME  - caracteres(30)
CPF - numerico(12)
EMAIL - caracteres(30)
TELEFONE - caracteres(30)
ENDERECO - caracteres(100)
SEXO - caracteres(1)

/* PROCESSOS DE MODELAGEM*/


1 e 2 adm de dados

MODELAGEM CONCEITUAL - RASCUNHO
MODELAGEM LÓGICA - QUALQUER PROGRAMA DE MODELAGEM

/* fase 3 - dba / ad */
MODELAGEM FISICA - 

\


/* INICIANDO A MODELAGEM FISICA*/

/* CRIANDO BANCO DE DADOS*/

CREATE DATABASE PROJETO;

/* CONCTANDO AO BANCO*/

USE PROJETO;

/* CRIANDO TABELA DE CLINETES*/

CREATE TABLE CLIENTE(
	NOME VARCHA(30),
	SEXO CHAR(1),
	EMAIL VARCHAR(30),
	CPF INT(11),
	TELEFONE VARCHAR(30),
	ENDERECO VARCHAR(100) 
);

/*MOSTRANDO AS TABELAS DO PROJETO*/

SHOW TABLES;

/DESCOBRINDO ESTRUTURA DE UMA TABELA/

DESC CLIENTE;

/* SINTAXE BASICA DE INSERCAO - INSERT INTO (TABELA) */

/*FORMA 01 - OMITINDO COLUNAS*/

INSERT INTO CLIENTE VALUES('CELIA', 'F','CELIA#GMAIL.COM',85985511569,'OSCAR CURY - BOM RETIRO - PATOS DE MINAS - MG ');
INSERT INTO CLIENTE VALUES('JOAO', 'M', 'JOAO@GMAIL.COM', 98987059698,'MAIA LACERDA - RIO DE JANEIRO - RJ');

/* FORMA 02 - COLOCANDO AS COLUNAS = (POSSO ESCOLHER A ORDEM QUE QUERO ENTRAR)*/

INSERT INTO CLIENTE(NOME, SEXO,ENDERECO,TELEFONE,CPF) VALUES ('LILIAN', 'F','RUA CANADEIS', '9999999999',999999999);

/* INSERT COMPACTO - SOMENTE SQL*/

INSERT INTO CLIENTE VALUES('ANA', 'F','ANA@GMAIL',999999998,'8989809', 'BRENIHO RUA DELE'),('ANAB', 'M','ANABH@GMAIL',999999008,'8649809', 'BRENIHO RUA DELE');

/*o comansdo select 
selecao projecao e juncao, PROJECAO POR COLUNAS
*/

SELECT NOW() ; /*PROJETA O QUE SE PEDIR*/ /*PODENDO USAR PARA CRIAR TABELAS FLASH, COM SELECT NOW() AS DATA_HORA; */
SELECT NOW() AS DATA_HORA;
SELECT 'FELIPE MAFRA';
SELECT 'BANCO DE DADOS';

/* ALIAS DE COLUNAS = MOSTRA TUDO*/

SELECT NOME, SEXO,EMAIL FROM CLIENTE;
SELECT NOME, SEXO, EMAIL, ENDERECO FROM CLIENTE;

SELECT * FROM CLIENTE; /*MOSTRA TODOS OS DA TABELA */

/*FILTROS*/

SELECT * FROM CLIENTE; /*TRARA A TABELA INTEIRA*/

/*USANDO OS FILTROS PARA MOSTRAR DADOS APARTIR DE CONDICOES DESEJADAS*/

SELECT NOME, SEXO FROM CLIENTE
WHERE SEXO = 'M'; /*CONDICAO DESEJADA*/

SELECT NOME, SEXO FROM CLIENTE
WHERE SEXO = 'F';

SELECT NOME, SEXO FROM CLIENTE
WHERE ENDERECO = 'RJ';

/*UTILIZANDO O LIKE*/

SELECT NOME, SEXO FROM CLIENTE
WHERE ENDERECO LIKE 'RJ'; /*ELE USA O LIKE COMO SE FOSSE APROXIMADO, QUE TENHA NO DADO BUSCADO*/

/*CARACTERE CORINGA % -> QUALQUER COISA */
SELECT NOME, SEXO FROM CLIENTE
WHERE ENDERECO LIKE '%RJ'; /*QUER DIZER QUE PODE COMECAR COM QLQER COISA MAS TEM QUE TERMINAR COM RJ O USO PODE SER DE ACORDO COM A PRECISAO*/

/*EXERCICIO1*/

CREATE DATABASE LIVRARIA;

USE LIVRARIA;

CREATE TABLE LIVROS(
	NOME_LIVRO VARCHAR(50),
	NOME_EDIT VARCHAR(50),
	VALOR CHAR(10);
	NUMERO_PAG CHAR(10),
	NOME_AUTOR VARCHAR(50),
	SEXO_AUTOR CHAR(1),
	UF_LIVRO CHAR(2)

);

INSERT INTO LIVROS VALUES('HARRY PORRA','MADARA SONICS','225.20','400','BRENO',
INSERT INTO LIVROS VALUES('MAMBA MENTALITYS','EDITORA EGGS',29.50,'500','EH O BRAYA','RJ');
INSERT INTO LIVROS VALUES('LOLO MASTER','EDITORA HUA',45.50,'400','TECO TECO','SP');

SELECT COUNT(*) FROM CLIENTE; /*CONTARA O NUMERO DE RWEGISTROS DE CLIENTE*/
SELECT COUNT(*) AS "QUANTIDADE DE REGISTROS DA TAB. CLIENTE"
FROM CLIENTE; /*COM O AS EU POSSO RENOMEAR*/

SELECT SEXO, COUNT(*)
FROM CLIENTE
GROUP BY SEXO /* EM CASO DE CONTAR COISAS ESPECIFICAS, USAR GROUP BY OARA REFERENCIAR, CASO O CONTRARIO O COUNT IRA CONTAR TODOS OS CAMPOS, IRA AGRUPAR E DIVIDIR EM CADA CASO*/


mysql> SELECT SEXO, COUNT(*)
    -> FROM CLIENTE
    -> GROUP BY SEXO;
+------+----------+
| SEXO | COUNT(*) |
+------+----------+
| F    |        3 |
| M    |        2 |
+------+----------+
2 rows in set (0.03 sec)

/*EXERCICIO 26 */

SELECT COUNT(*) FROM FUNCIONARIOS;
/*1*/

SELECT NOME, IDFUNCIONARIO, DEPARTAMENTO FROM FUNCIONARIOS
WHERE DEPARTAMENTO = 'ROUPAS' OR DEPARTAMENTO = 'FILMES';

SELECT COUNT(*), DEPARTAMENTO
FROM FUNCIONARIOS
GROUP BY DEPARTAMENTO
ORDER BY 1;

/*2*/

SELECT NOME, DEPARTAMENTO, EMAIL FROM FUNCIONARIOS
WHERE DEPARTAMENTO = 'FILMES' AND DEPARTAMENTO = 'LAR';

/*3*/

SELECT NOME, SEXO, DEPARTAMENTO FROM FUNCIONARIOS
WHERE DEPARTAMENTO = 'JARDIM' OR SEXO = 'M';


SELECT NOME, EMAIL,DEPARTAMENTO FROM FUNCIONARIOS
WHERE (SEXO = "FEMININO" AND DEPARTAMENTO = "LAR") OR (SEXO = "FEMININO" AND DEPARTAMENTO = "FILMES"); /*INVERTER*/


SELECT NOME, EMAIL,DEPARTAMENTO FROM FUNCIONARIOS
WHERE (SEXO = "FEMININO");

/*para casos de buscas por campos nulos = NULL*/

SELECT * FROM CLIENTE
WHERE EMAIL IS NULL;

SELECT * FROM CLIENTE
WHERE EMAIL IS NOT NULL;

/* USANDO UPDATE PARA ATUALIZAR REGISTROS NA TABELA*/

SELECT NOME, EMAIL 
FROM CLIENTE;

UPDATE CLIENTE
SET EMAIL = "NOVOEMAIL.COM"
WHERE NOME = "LILIAN"; 

/*DELETANDO REGISTROS COM A CLAUSULA DELETE, USE SEMPRE COM WHERE PARA QUE NAO OCORRA DELETACAO TOTAL DO BANCO*/

DELETE FROM CLIENTE;

SELECT COUNT(*) FROM CLIENTE; /*CONTAR PARA TER CERTEZA */
SELECT * FROM CLIENTE WHERE NOME = "ANA";

DELETE FROM CLIENTE
WHERE NOME = "ANA";

/*PRIMEIRA FORMA NORMAL*/

/*
1 - TODO CAMPO VETORIZADO SE TORNARA OUTRA TABELA
[AMARELO, AZUL,LARANJA,VERDE] -> CORES
[KA, FIESTA, UNO, CIVIC] - > CARROS

2 - TODO CAMPO MULTIVALORADO SE TORNARA OUTRA TABELA.
QUANDO O CAMPO FOR DIVISIVEL

3 - TODA TABELA NECESSTA DE PELO MENOS UM CAMPO QUE IDENTIFIQUE TODO O REGISTRO COMO SENDO UNICO.
ISSO SE CHAMA DE CHAVE PRIMARIA OU PRIMARY KEY

	CHAVE NATURAL - CHAVE QUE PERTENCE AO REGISTRO X: (CPF)
	CHAVE ARTIFICIAL - CHAVE CRIADA EX: (ID)

*/
CREATE DATABASE COMERCIO;

USE COMERCIO;

SHOW TABLES;

/*QUEM CONTROLA A CHAVE EH O BANCO*//*NOT NULL TORNA OBRIGATORIO A COLUNA*//*UNIQUE DEIXA OS CAMPOS UNCOS*/
CREATE TABLE CLIENTE(
	IDCLIENTE INT PRIMARY KEY AUTO_INCREMENT, 
	NOME VARCHAR(30) NOT NULL, 
	SEXO ENUM('F', 'M')  NOT NULL,
	EMAIL VARCHAR(50) UNIQUE,
	CPF VARCHAR(15) UNIQUE
);

CREATE TABLE ENDERECO(
	IDENDERECO INT PRIMARY KEY AUTO_INCREMENT,
	BAIRRO VARCHAR(30) NOT NULL,
	RUA VARCHAR(30) NOT NULL,
	CIDADE VARCHAR(30) NOT NULL,
	ESTADO CHAR(2) NOT NULL
	
);

CREATE TABLE TELEFONE(
	IDTELEFONE INT PRIMARY KEY AUTO_INCREMENT,
	TIPO ENUM('RES', 'COM','CEL') NOT NULL,
	NUMERO VARCHAR(10) NOT NULL

);












































































