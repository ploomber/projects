DROP TABLE IF EXISTS {{ product }};
CREATE TABLE {{ product }} AS
SELECT name, sum(number) AS number
FROM `bigquery-public-data.usa_names.usa_1910_2013`
GROUP BY name
