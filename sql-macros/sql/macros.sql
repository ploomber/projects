{% macro agg(col_group, col_agg, from_table) -%}

SELECT
    {{col_group}},
{% for fn in ['AVG', 'MAX', 'MIN'] %}
    {{fn}}({{col_agg}}) as {{fn}}_{{col_agg}}{{ ',' if not loop.last else '' }}
{% endfor %}
FROM {{from_table}}
GROUP BY {{col_group}}

{%- endmacro %}