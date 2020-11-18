DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
SELECT PostId, count(*) AS count
FROM {{upstream['upload-comments']}}
GROUP BY PostId