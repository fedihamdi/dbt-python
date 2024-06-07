-- Example test for customer data
SELECT COUNT(*)
FROM {{ ref('customer_orders') }}
WHERE total_orders < 0;
