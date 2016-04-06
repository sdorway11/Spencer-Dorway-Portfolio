
CREATE PROCEDURE spFindAuthorBooks @AuthorName varchar(30) = '', @Location varchar(30) = ''
AS

	SELECT B.Title, COUNT(BC.No_Of_Copies) AS 'Number of Copies Owened'
		FROM Book_Authors AS BA inner join Book AS B
		ON BA.BookID = B.BookID
		inner join Book_Copies as BC
		ON B.BookID = BC.BookID
		inner join Library_Branch as LB
		ON BC.BranchID = LB.BranchID
		WHERE BA.AuthorName = @AuthorName and LB.BranchName = @Location
		GROUP BY B.Title
Go


EXEC spFindAuthorBooks 'Stephen King', 'Chapinero'