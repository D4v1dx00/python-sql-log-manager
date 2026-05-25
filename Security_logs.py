import pyodbc
try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=security_logs;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    cursor = conn.cursor()

    while True:
        print("--- Select option ---")
        print("1. Show users")
        print("2. Show logs")
        print("3. Add log")
        print("4. Show failed logs")
        print("5. Summary")
        print("6. Exit")
        choice = input("pick option: ").strip()

        if choice=="1":
            cursor.execute("SELECT * FROM dbo.users")
            rows= cursor.fetchall()

            for row in rows:
                print(row[1],"-",row[2]) 
        elif choice=="2":
            cursor.execute("select username,email,event_type,source_ip,event_time from users join logs on users.id = logs.user_id")
            rows= cursor.fetchall()

            for row in rows:
                print(row[0],"-",row[1],"-",row[2],"-",row[3],"-",row[4]) 
        elif choice=="3":
            user_id = input("user id: ").strip()
            event_type = input("event type: ").strip()
            source_ip = input("source ip: ").strip() 
            if not user_id.isnumeric():
                print("User id must be numeric!")
            else:
                cursor.execute("select * from users where id=?",(int(user_id),))
                rows = cursor.fetchall()
                if len(rows) > 0:
                    cursor.execute("insert into logs (user_id,event_type,event_time,source_ip) values (?,?,getdate(),?)",
                    (int(user_id),event_type, source_ip))
                    conn.commit()
                    print("Added")
                else:
                    print("User id does not exist")


        elif choice == "4":
            cursor.execute("select username,email,event_type,source_ip,event_time from users join logs on users.id = logs.user_id where event_type='login_failed' ")
            rows= cursor.fetchall()

            for row in rows:
                print(row[0],"-",row[1],"-",row[2],"-",row[3],"-",row[4])
        elif choice == "5":
            cursor.execute("select event_type, count(id) from logs group by event_type")
            rows= cursor.fetchall()
            for row in rows:
                print(row[0],": ",row[1])

        elif choice == "6":
            print("Program closed.")
            break
        else:
            print("Wrong option")
    conn.close()
except pyodbc.Error:
    print("Database connection failed")
