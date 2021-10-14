DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
SELECT * FROM prices
WHERE price > 100;
