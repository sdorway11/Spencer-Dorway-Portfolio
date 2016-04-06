SELECT LB.BranchName,Book.Title, B.Name, B.Address
FROM Library_Branch as LB inner join Book_Loans as BL
ON LB.BranchID = BL.BranchID
inner join Borrower as B
ON BL.CardNo = B.CardNo
inner join Book 
on Book.BookID = BL.BookID
WHERE LB.BranchName = 'Sharpstown' and BL.DueDate = '2016-01-29'