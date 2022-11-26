SELECT * FROM brides;
SELECT * FROM dresses;
SELECT * FROM employees;
SELECT * FROM to_do_items;
SELECT * FROM orders;
SELECT * FROM measurements;

INSERT INTO employees (first_name, last_name, title, permission, hire_date, password, created_at, updated_at)
VALUES ("Madina", "Skandari", "Boss", 5, 11/1/2019, "password1", NOW(), NOW() );

ALTER TABLE to_do_items
ADD COLUMN status varchar(15)
AFTER notes;

UPDATE orders
SET status = "archived"
WHERE id = 4;

SELECT * FROM to_do_items 
LEFT JOIN employees
ON to_do_items.employee_id = employees.id
WHERE employees.id = 1
AND status = "active" ;

SELECT orders.id, brides.first_name AS brfname, brides.last_name AS brlname, name, orders.notes AS order_notes, employees.first_name AS taken_by FROM orders 
            LEFT JOIN brides ON brides.id = orders.bride_id 
            LEFT JOIN dresses ON dresses.id = orders.dress_id
            LEFT JOIN employees ON employees.id = orders.employee_id
            WHERE orders.status = "archived";
            
DELETE FROM employees WHERE id = 2;
