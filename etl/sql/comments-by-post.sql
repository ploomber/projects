DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
SELECT PostId, count(*)
FROM {{upstream['upload_comments']}}
GROUP BY PostId