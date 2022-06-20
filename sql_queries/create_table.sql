DROP TABLE IF EXISTS estates;

CREATE TABLE estates (
	id serial NOT NULL PRIMARY KEY,
	info json NOT NULL
);