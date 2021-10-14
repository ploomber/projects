DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
SELECT Id, LENGTH(body) AS length
FROM {{upstream['upload-posts']}}
GROUP BY Id