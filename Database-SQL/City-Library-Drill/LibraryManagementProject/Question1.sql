SELECT LB.BranchName, B.Title, BC.No_Of_Copies
FROM Library_Branch as LB inner join Book_Copies as BC
on LB.BranchID = BC.BranchID
inner join Book as B 
on BC.BookID = B.BookID
Where B.Title = 'The Lost Tribe' and LB.BranchName = 'Sharpstown'