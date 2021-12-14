CREATE TABLE intuitivecare_test3.demonstracoes_contabeis (
	id int primary key not null auto_increment,
	data DATE NOT NULL,
	reg_ans DECIMAL(6, 0) NOT NULL,
	cd_conta_contabil DECIMAL(10, 0) NOT NULL,
	descricao VARCHAR(255) NOT NULL,
	vl_saldo_final DECIMAL(15, 2) NOT NULL,
    data_de_criacao TIMESTAMP DEFAULT current_timestamp,
    data_de_atualizacao DATETIME DEFAULT current_timestamp ON UPDATE current_timestamp
);
