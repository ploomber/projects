DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
SELECT product_id, count * price AS revenue
FROM {{upstream['group_sales.sql']}}
JOIN {{upstream['filter_prices.sql']}}
USING (product_id);
