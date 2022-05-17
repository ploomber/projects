DROP VIEW IF EXISTS {{ product }};
CREATE VIEW {{ product }} AS
SELECT *
FROM {{ upstream["create-table"] }}