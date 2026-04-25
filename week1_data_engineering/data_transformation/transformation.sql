-- Convert InvoiceDate format
SELECT *,
       CAST(InvoiceDate AS DATETIME) AS CleanDate
FROM retail;