USE security_logs;
GO

INSERT INTO dbo.users (username, email)
VALUES
('alice', 'alice@example.com'),
('bob', 'bob@example.com'),
('charlie', 'charlie@example.com');
GO

INSERT INTO dbo.logs (user_id, event_type, event_time, source_ip)
VALUES
(1, 'login_success', SYSDATETIME(), '192.168.1.10'),
(2, 'login_failed', SYSDATETIME(), '10.0.0.5'),
(3, 'file_download', SYSDATETIME(), '172.16.0.15');
GO