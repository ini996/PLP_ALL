
-- 1. Create the expenses table
CREATE TABLE IF NOT EXISTS expenses (
    id INT PRIMARY KEY,
    description VARCHAR(255),
    category VARCHAR(100),
    amount DECIMAL(10,2),
    payment_method VARCHAR(50),
    expense_date DATE
);

-- 2. Insert sample data
INSERT INTO expenses (id, description, category, amount, payment_method, expense_date) VALUES
(1, 'Grocery shopping',    'Food',          125.50, 'Card', '2025-05-01'),
(2, 'Movie night',         'Entertainment',  55.00, 'Cash', '2025-05-05'),
(3, 'Electricity bill',    'Utilities',     300.00, 'Card', '2025-05-03'),
(4, 'Lunch with friends',  'Food',           95.00, 'Cash', '2025-05-06'),
(5, 'Internet recharge',   'Utilities',     250.00, 'Card', '2025-05-02')
ON DUPLICATE KEY UPDATE
    description = VALUES(description),
    category = VALUES(category),
    amount = VALUES(amount),
    payment_method = VALUES(payment_method),
    expense_date = VALUES(expense_date);

-- 3. Query with WHERE, wildcards, logical and comparison operators, and ORDER BY
SELECT id, description, category, amount, expense_date
FROM expenses
WHERE 
    (description LIKE '%lunch%' OR description LIKE '%grocery%') -- wildcards
    AND amount >= 100                                             -- comparison
    AND category != 'Entertainment'                               -- logical NOT
ORDER BY expense_date DESC;                                       -- order latest first
