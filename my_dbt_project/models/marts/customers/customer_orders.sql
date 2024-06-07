-- Example SQL transformation for customer orders
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM
    {{ ref('stg_customers') }} c
LEFT JOIN
    {{ ref('stg_orders') }} o
ON
    c.customer_id = o.customer_id
GROUP BY
    c.customer_id, c.customer_name;
