DROP TABLE IF EXISTS {{ product }};
CREATE TABLE {{ product }} AS
SELECT *
FROM `bigquery-public-data.usa_names.usa_1910_2013`
LIMIT 100000