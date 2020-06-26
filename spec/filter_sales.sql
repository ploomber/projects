DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
SELECT * FROM sales
WHERE product_id != 90;
