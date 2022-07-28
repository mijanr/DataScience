SELECT DISTINCT 
    * 
FROM 
    public.iris_dataset 
WHERE 
    --"sepal.length" > 5.0 AND
    --"sepal.width" > 3.0 AND 
    --"variety" IN ('Setosa', 'Virginica')
    "sepal.length" BETWEEN 5.0 AND 6.0 
ORDER BY 
    "sepal.length" ASC--DESC
FETCH FIRST 50 ROWS ONLY; --same as LIMIT. To make it compatable with other SQL databases
--LIMIT 10;
--print the shape of the data
--SELECT COUNT(*) number_of_rows FROM public.iris_dataset
