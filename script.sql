INSERT INTO tb_usuario(login,senha) VALUES
('admin', 'admin'),
('joao', '123456');

CREATE TABLE tb_usuario(
	codigo_usuario SERIAL PRIMARY KEY,
	login VARCHAR(200) NOT NULL,
	senha VARCHAR (200) NOT NULL
);	


SELECT * from tb_usuario;