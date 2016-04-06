SELECT LB.BranchName, COUNT(BL.BranchID) as 'Total Number of Books'
from Book_Loans as BL 
inner join Library_Branch as LB
on BL.BranchID = LB.BranchID
Group by LB.BranchName