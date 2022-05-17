SELECT name,
    SUM(number) as total_people
FROM {{upstream["transform"]}}
GROUP BY name,
    state
ORDER BY total_people DESC
LIMIT 20