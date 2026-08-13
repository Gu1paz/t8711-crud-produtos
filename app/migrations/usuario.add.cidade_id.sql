alter table usuario add column cidade_id integer not null;
alter table usuario add constraint fk_cidade_usuario foreign key(cidade_id) references cidade(id);

