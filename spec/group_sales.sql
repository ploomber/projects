DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
SELECT product_id, count(*) as count
FROM {{upstream['filter_sales']}}
GROUP BY product_id;
