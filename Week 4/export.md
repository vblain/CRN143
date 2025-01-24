docker exec -it my_postgres psql -U vblain -d sqlda2

CREATE TEMP VIEW top_cities AS (SELECT city, count(1) AS number_of_customers FROM customers WHERE city IS NOT NULL GROUP BY 1 ORDER BY 2 desc limit 10 );

\COPY (SELECT * FROM top_cities) TO '/temp/top_cities.csv' WITH CSV HEADER DELIMITER ';'

drop view top_cities;
