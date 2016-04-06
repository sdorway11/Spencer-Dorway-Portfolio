SELECT B.Name, COUNT(BL.CardNo) AS TOTAL
FROM Book_Loans AS BL inner join Borrower AS B
ON BL.CardNo = B.CardNo
GROUP BY B.Name
HAVING COUNT(*) > 5