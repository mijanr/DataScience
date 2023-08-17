-- -- create a new table called iris_data in postgres database
-- CREATE TABLE iris_table (
--     sepal_length DOUBLE PRECISION,
--     sepal_width DOUBLE PRECISION,
--     petal_length DOUBLE PRECISION,
--     petal_width DOUBLE PRECISION,
--     species TEXT
-- );

--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**

-- -- copy data from csv file to postgres database
--COPY iris_table FROM '/tmp/iris_data.csv' DELIMITER ',' CSV HEADER;

--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**

-- -- check if data is copied, show first 5 rows
SELECT * FROM iris_table LIMIT 5;

----**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**
-- group by species and show the count of each species
SELECT species, COUNT(*) FROM iris_table GROUP BY species;

----**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**
-- rename the columns
SELECT species, AVG(sepal_length) AS avg_sepal_length, AVG(sepal_width) AS avg_sepal_width, AVG(petal_length) AS avg_petal_length, AVG(petal_width) AS avg_petal_width FROM iris_table GROUP BY species;

----**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**
-- Select all the data points that are greater than the average of the individual features. Then 
SELECT * FROM iris_table WHERE sepal_length > (SELECT AVG(sepal_length) FROM iris_table) AND sepal_width > (SELECT AVG(sepal_width) FROM iris_table) AND petal_length > (SELECT AVG(petal_length) FROM iris_table) AND petal_width > (SELECT AVG(petal_width) FROM iris_table);

----**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**
-- export the data to a csv file.
--COPY (SELECT * FROM iris_table WHERE sepal_length > (SELECT AVG(sepal_length) FROM iris_table) AND sepal_width > (SELECT AVG(sepal_width) FROM iris_table) AND petal_length > (SELECT AVG(petal_length) FROM iris_table) AND petal_width > (SELECT AVG(petal_width) FROM iris_table)) TO '/tmp/iris_data_greater_than_avg.csv' DELIMITER ',' CSV HEADER;

----**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**
-- comprehensive summary of the data
SELECT
    species,
    COUNT(*) AS total_count,
    AVG(sepal_length) AS avg_sepal_length,
    AVG(sepal_width) AS avg_sepal_width,
    AVG(petal_length) AS avg_petal_length,
    AVG(petal_width) AS avg_petal_width,
    MIN(sepal_length) AS min_sepal_length,
    MIN(sepal_width) AS min_sepal_width,
    MIN(petal_length) AS min_petal_length,
    MIN(petal_width) AS min_petal_width,
    MAX(sepal_length) AS max_sepal_length,
    MAX(sepal_width) AS max_sepal_width,
    MAX(petal_length) AS max_petal_length,
    MAX(petal_width) AS max_petal_width
FROM
    iris_table
GROUP BY
    species
ORDER BY
    species;
