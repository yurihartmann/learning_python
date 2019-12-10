drop table pessoa;
drop table trabalhador;
drop table linguagem_de_programacao;
drop table equipe;
drop table equipe_trabalhador;

CREATE TABLE pessoa(
	cd_pessoa int not NULL AUTO_INCREMENT,
	PRIMARY KEY(cd_pessoa),
	nm_pessoa varchar(100) not null,
	vl_idade int not null
);

CREATE TABLE trabalhador(
	cd_trabalhador int not NULL AUTO_INCREMENT,
	PRIMARY KEY(cd_trabalhador),
	fk_pessoa int not null,
	FOREIGN KEY (fk_pessoa) REFERENCES pessoa(cd_pessoa),
	nm_cargo varchar(200),
	vl_salario FLOAT(8,2)
);

CREATE TABLE linguagem_de_programacao(
	cd_linguagem int not null AUTO_INCREMENT,
	PRIMARY KEY(cd_linguagem),
	nm_linguagem varchar(100)
);

CREATE TABLE equipe(
	cd_equipe int not null AUTO_INCREMENT,
	PRIMARY KEY(cd_equipe),
	nm_equipe varchar(100),
	fk_linguagem int not NULL,
	FOREIGN KEY(fk_linguagem) REFERENCES linguagem_de_programacao(cd_linguagem)
);

CREATE TABLE equipe_trabalhador(
	fk_equipe int not null,
	fk_trabalhador int not null,
	PRIMARY KEY(fk_equipe, fk_trabalhador),
	FOREIGN KEY(fk_equipe) REFERENCES equipe(cd_equipe) ON DELETE CASCADE ,
	FOREIGN KEY(fk_trabalhador) REFERENCES trabalhador(cd_trabalhador)
);