SELECT o.*
FROM orders o
JOIN order_status os on o.order_status_id = os.order_status_id
WHERE os.status_name = 'Finished';
