<!-- --------Coding Skills Assessment-------- -->

Project Description
This project provides a solution for an e-commerce system that manages users, products, orders, and payments. It includes business logic for inventory management and SQL queries for analyzing customer and book purchase data from an online bookstore.

Project Structure
System Design: Contains class definitions for User, Product, Order, and Payment.
Business Logic: Includes functions to process orders and restock inventory.
Database Queries: SQL queries to analyze sales data in an online bookstore.

Prerequisites
Python 3.x
SQL database (e.g., SQLite, MySQL)

How to run the project
1. System Design
The classes for users, products, orders, and payments are implemented in the file system_design.py. The class relationships follow standard e-commerce system structures, allowing users to place orders, each order containing multiple products, with one payment per order.

2. Business Logic Implementation
The business logic is implemented in the file business_logic.py.
The process_orders() function handles incoming sales orders and reduces stock levels accordingly.
The restock_items() function updates the stock for products that have fallen below a restocking threshold.

3. Database Queries
The SQL queries are included in the file database_queries.sql. These queries are designed for an online bookstore and can be run in any SQL environment that contains the following tables:

Customers: customer_id, name, email
Books: book_id, title, author, price
Orders: order_id, customer_id, order_date
OrderDetails: order_id, book_id, quantity

4. Diagrams
The class diagram is included as class_diagram.png and shows the relationships between User, Product, Order, and Payment.