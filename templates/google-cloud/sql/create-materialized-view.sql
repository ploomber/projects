DROP MATERIALIZED VIEW IF EXISTS {{ product }};
CREATE MATERIALIZED VIEW {{ product }} AS
SELECT *
FROM {{ upstream["create-table"] }}
