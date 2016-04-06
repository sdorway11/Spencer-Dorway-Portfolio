SELECT B.Name, B.CardNo, DateOut
FROM Borrower as B left join Book_Loans as BL
on B.CardNo = BL.CardNo
WHERE BL.DateOut is null
