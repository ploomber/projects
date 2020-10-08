-- this placeholder will be replaced at runtime
DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
SELECT product_id, count * price AS revenue
-- declare dependencies using the name (or source if no name was declared)
-- of the task that should run first
FROM {{upstream['group_sales']}}
JOIN {{upstream['filter_prices']}}
USING (product_id);
