# Security Logs Manager

A simple Python CLI tool for managing and viewing security-related logs stored in a SQL Server database. This project was created to practice Python basics, SQL queries, database connections with `pyodbc`, and simple security-oriented log handling.

## Features

- connect to a SQL Server database
- display users from the `users` table
- display logs joined with user information
- add new log entries
- show failed login events
- display a summary of log event counts 
- basic validation for user input
- handle database connection errors

## Requirements

- Python 3.x
- `pyodbc`
- ODBC Driver 18 for SQL Server
- SQL Server running locally
- database named `security_logs`

## How to run

```bash
python main.py
```