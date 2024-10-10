-- Books ordered more than 10 times
SELECT b.title, SUM(od.quantity) AS total_quantity
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
GROUP BY b.book_id
HAVING total_quantity > 10;
