DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
SELECT * FROM my_table
WHERE some_value is not null AND age > 0