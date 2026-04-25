-- Create indexes for faster queries
CREATE INDEX idx_customer ON retail(CustomerID);
CREATE INDEX idx_invoice ON retail(InvoiceNo);