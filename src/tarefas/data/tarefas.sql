CREATE DATABASE IF NOT EXISTS 'arefas';

USE 'tarefas';

DROP TABLE IF EXISTS 'tarefas';

CREATE TABLE IF NOT EXISTS 'tarefas' (
    'idTarefa' BIGINT NOT NULL  PRIMARY KEY,
    'tituloTarefa' VARCHAR(255) NOT NULL,
    'dataConclusao' DATE,
);
