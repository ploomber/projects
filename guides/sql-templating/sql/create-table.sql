-- import macros
{% import "macros.sql" as m %}

DROP TABLE IF EXISTS {{product}};

CREATE TABLE {{product}} AS
-- use macro
{{m.agg(col_group='country', col_agg='price', from_table='sales')}}
