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

--SELECT title AS BookTitle, Members.name AS MemberName, loan_date AS LoanDate
--FROM Loans JOIN  Members ON Members.id = member_id RIGHT JOIN Books ON Books.id = Loans.book_id
--ORDER BY BookTitle;

-- 3. **Branches and books**  
-- List all library branches and the books they hold.

--SELECT name AS Branch, title AS Books
--FROM LibraryBranch LEFT JOIN Books ON LibraryBranch.id = Books.branch_id;

-- 4. **Branch book counts**  
-- Show each library branch and the number of books it holds.

--SELECT name AS Branch, COUNT(title) AS NumberOfBooks
--FROM LibraryBranch LEFT JOIN Books ON LibraryBranch.id = Books.branch_id
--GROUP BY Branch
--ORDER BY NumberOfBooks DESC;

-- 5. **Branches with more than 7 books**  
-- Show branches that hold more than 7 books.

--SELECT name AS Branch, COUNT(title) AS NumberOfBooks
--FROM LibraryBranch LEFT JOIN Books ON LibraryBranch.id = Books.branch_id
--GROUP BY Branch
--HAVING NumberOfBooks > 7;

-- 6. **Members and loans**  
-- List all members and the number of loans they have made.

--SELECT name AS Member, COUNT(Loans.id) AS NumberOfLoans
--FROM Members LEFT JOIN Loans ON Members.id = Loans.member_id
--GROUP BY Member
--ORDER BY NumberOfLoans DESC; 

-- 7. **Members who never borrowed**  
-- Identify members who have never borrowed a book.

--SELECT name AS Member
--FROM Members LEFT JOIN Loans ON Members.id = Loans.member_id
--GROUP BY Member
--HAVING COUNT(Loans.id) = 0;

-- 8. **Branch loan totals**  
-- For each library branch, show the total number of loans for books in that branch.

--SELECT name AS Branch, COUNT(Loans.id) as NumberOfLoans
--FROM LibraryBranch LEFT JOIN Books ON LibraryBranch.id = Books.branch_id
--LEFT JOIN Loans ON Books.id = Loans.book_id
--GROUP BY Branch
--ORDER BY NumberOfLoans DESC;

-- 9. **Members with active loans**  
-- List members who currently have at least one active loan.

--SELECT name AS MembersWithActiveLoans
--FROM Members LEFT JOIN Loans ON Members.id = Loans.member_id
--GROUP BY MembersWithActiveLoans
--HAVING COUNT(Loans.id) > 0;

-- 10. **Books and loans report**  
-- Show all books and all loans, including books that were never loaned.
-- Include a column classifying each row as “Loaned book” or “Unloaned book.”.
-- You will need to look up how to do this (hint: a case statement would work).
-- Also, display if any loans are overdue.

SELECT Books.title AS Book, CASE 
                                WHEN Loans.member_id IS NULL THEN 'Unloaned Book'
                                ELSE 'Loaned Book'
                            END AS LoanStatus,
        Members.name AS Borrower,
                            CASE
                                WHEN Loans.member_id IS NULL THEN ''
                                WHEN Loans.return_date < CURRENT_DATE THEN 'Overdue'
                                ELSE 'Not overdue'
                            END AS OverdueStatus
FROM Books LEFT JOIN Loans ON Books.id = Loans.book_id
LEFT JOIN Members ON Members.id = Loans.member_id;










