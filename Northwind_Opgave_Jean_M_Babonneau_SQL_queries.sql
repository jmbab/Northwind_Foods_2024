-- ............................
-- SQL OPGAVE NORTHWIND del 1
-- JM BABONNEAU - 25-10-2024
-- ............................

/* List all products from the Products table 
and sort them in descending order by the UnitPrice field */

SELECT *
FROM products
ORDER BY UnitPrice DESC;

/* Find all customers from the UK and Spain.
Use the Customers table
Result: 12 Rows */

SELECT * 
FROM customers 
WHERE Country IN ('UK', 'Spain');


/* Find all Products where we have more than 100 in stock (UnitsInStock) 
and the price (UnitPrice) is greater than or equal to 25.
Use the Products table.
/// Result: 10 Rows /// I GOT ONLY 2 RESULTS!  */

SELECT *
FROM products
WHERE UnitsInStock > 100
AND UnitPrice >= 25;


/* Find all countries an order has been sent to, show them only once
Use the Orders table
Result: 21 Rows */

SELECT DISTINCT ShipCountry 
FROM Orders;


/* Find all orders that have an OrderDate in month 10 of 1996.
Use the Orders table.
Result: 26 Rows */

SELECT * 
FROM Orders 
WHERE OrderDate BETWEEN '1996-10-01' AND '1996-10-31';


/* Find all orders where ShipRegion is blank, ShipCountry = Germany, 
Freight is greater than or equal to 100, EmployeeID = 1 
and OrderDate is from 1996.
Use the Orders table.
Result: 2 Rows */

SELECT * 
FROM Orders
WHERE (ShipRegion IS NULL OR ShipRegion = '')
AND ShipCountry = 'Germany' 
AND Freight >= 100 
AND EmployeeID = 1
AND OrderDate BETWEEN '1996-01-01' AND '1996-12-31';


/* Find the orders that are not delivered on time, 
ShippedDate is greater than RequiredDate
Use the Orders table.
Result: 37 Rows */

SELECT * 
FROM Orders
WHERE ShippedDate > RequiredDate;


/* Find all Orders (OrderDate) from 1997 in the months of 
January, February, March and April from Canada (ShipCountry)
Use the Orders table.
Result: 8 Rows */

SELECT * 
FROM Orders
WHERE OrderDate BETWEEN '1997-01-01' AND '1997-04-30'
AND ShipCountry = 'Canada';


/* Find the orders where EmployeeID is equal to 2, 5 or 8. 
ShipRegion is not ' ' and ShipVia is either 1 or 3. 
Must be sorted first by EmployeeID then ShipVia both ascending
Use the Orders table.
Result: 57 Rows */

SELECT * 
FROM Orders 
WHERE EmployeeID IN (2, 5, 8)
  AND ShipRegion != ''
  AND ShipVia IN (1, 3)
ORDER BY EmployeeID ASC, ShipVia ASC;


/* Find the Employees where there is no value (' ') 
in Region or ReportsTo is "blank" (NULL) 
Furthermore, they must have been born in 1960 or earlier
Use the Employees table.
Result: 3 Rows */

SELECT * 
FROM Employees 
WHERE (Region IS NULL)
AND BirthDate <= '1960-12-31';


