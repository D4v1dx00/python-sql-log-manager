CREATE DATABASE security_logs;
GO

USE security_logs;
GO

CREATE TABLE dbo.users (
    id INT PRIMARY KEY IDENTITY(1,1),
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);
GO

CREATE TABLE dbo.logs (
    id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    event_time DATETIME2(7) NOT NULL,
    source_ip VARCHAR(45) NOT NULL,
    CONSTRAINT FK_logs_users FOREIGN KEY (user_id) REFERENCES dbo.users(id)
);
GO
