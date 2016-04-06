SELECT BA.AuthorName, COUNT(BC.No_Of_Copies) AS 'Number of Copies Owened'
FROM Book_Authors AS BA inner join Book AS B
ON BA.BookID = B.BookID
inner join Book_Copies as BC
ON B.BookID = BC.BookID
inner join Library_Branch as LB
ON BC.BranchID = LB.BranchID
WHERE BA.AuthorName = 'Stephen King' and LB.BranchName = 'Central'
GROUP BY BA.AuthorName