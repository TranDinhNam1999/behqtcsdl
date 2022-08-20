USE [BHOL]
GO
CREATE LOGIN bhol with PASSWORD=N'password', DEFAULT_DATABASE=[BHOL], CHECK_EXPIRATION=ON, CHECK_POLICY=ON;
GO
USE [BHOL]
GO
CREATE USER [bhol] FROM LOGIN [bhol];
GO
ALTER ROLE [db_owner] ADD MEMBER [bhol];
GO