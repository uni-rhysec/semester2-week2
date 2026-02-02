-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit

-- write your sql code here

-- 1. **List all loans**  
-- Show book title, member name, and loan date.

--SELECT title AS BookTitle, Members.name AS MemberName, loan_date AS LoanDate
--FROM Loans JOIN  Members ON Members.id = member_id JOIN Books ON Books.id = Loans.book_id;

-- 2. **Books and loans**  
-- List all books and any loans associated with them.

SELECT title AS BookTitle, Members.name AS MemberName, loan_date AS LoanDate
FROM Loans JOIN  Members ON Members.id = member_id RIGHT JOIN Books ON Books.id = Loans.book_id;


