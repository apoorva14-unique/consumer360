CREATE TABLE fact_sales (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice FLOAT,
    CustomerID FLOAT
);

CREATE TABLE dim_customer (
    CustomerID FLOAT PRIMARY KEY,
    Country VARCHAR(50)
);

CREATE TABLE dim_product (
    StockCode VARCHAR(20) PRIMARY KEY,
    Description VARCHAR(255)
);