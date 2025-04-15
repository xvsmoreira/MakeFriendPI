DROP TABLE IF EXISTS pets;

CREATE TABLE pets (
    id INTEGER PRIMARY KEY,
    foto BLOB,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    historia TEXT NOT NULL,
    tutor TEXT NOT NULL,
    telefone INTEGER NOT NULL,
    cep TEXT NOT NULL,
    rua TEXT NOT NULL,
    numero INTEGER NOT NULL,
    complemento TEXT,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL
);