CREATE TABLE tipo_produto(
	cd_tipo_produto int not null AUTO_INCREMENT,
	PRIMARY KEY(cd_tipo_produto),
	nm_tipo_produto varchar(50)
);


CREATE TABLE produto(
	cd_produto int not null AUTO_INCREMENT,
	PRIMARY KEY(cd_produto),
	fk_tipo_produto int not NULL,
	FOREIGN KEY(fk_tipo_produto) REFERENCES tipo_produto(cd_tipo_produto),
	nm_produto varchar(50),
	vl_preco float(8,2)
);