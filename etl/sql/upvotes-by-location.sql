DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
SELECT Location, AVG(upvotes) AS mean_upvotes
FROM {{upstream['upload-users']}}
GROUP BY Location
HAVING AVG(upvotes) > 1