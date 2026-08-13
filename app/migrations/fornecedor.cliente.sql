create table fornecedor
(
	id integer not null auto_increment,
	razao_social varchar(100) not null,
	nome_fantasia varchar(100) not null,
	cnpj varchar(20) not null,
	sla_atendimento int not null,
	primary key(id)
);

