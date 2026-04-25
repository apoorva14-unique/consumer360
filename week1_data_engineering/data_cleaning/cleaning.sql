-- Remove records with NULL CustomerID
SELECT *
FROM retail
WHERE CustomerID IS NOT NULL;

-- Remove negative or zero quantity
SELECT *
FROM retail
WHERE Quantity > 0;

-- Create Revenue column
SELECT *,
       Quantity * UnitPrice AS Revenue
FROM retail;