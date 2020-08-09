DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
SELECT Id, LENGTH(body) AS length
FROM {{upstream['upload_posts']}}
GROUP BY Id