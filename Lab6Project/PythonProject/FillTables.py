import pymysql.cursors

connection = pymysql.connect(db='ford_db', user='admin', passwd='admin', host='localhost', port=3333)

with connection:
    cursor = connection.cursor()

    fill_clients_table_query = """
        INSERT INTO Clients (ClientCompany, CheckingAccount, PhoneNumber, ContactPerson, Address) VALUES
        ('Company1', 'Account1', '123-456-7890', 'Person1', 'Address1'),
        ('Company2', 'Account2', '234-567-8901', 'Person2', 'Address2'),
        ('Company3', 'Account3', '345-678-9012', 'Person3', 'Address3'),
        ('Company4', 'Account4', '456-789-0123', 'Person4', 'Address4'),
        ('Company5', 'Account5', '567-890-1234', 'Person5', 'Address5'),
        ('Company6', 'Account6', '678-901-2345', 'Person6', 'Address6');
        """

    fill_cars_table_query = """
        INSERT INTO Cars (CarBrand, CarPrice, ClientID) VALUES
        ('Brand1', 25000.00, 1),
        ('Brand2', 30000.00, 2),
        ('Brand3', 35000.00, 3),
        ('Brand4', 40000.00, 4);
        """

    fill_repairs_table_query = """
        INSERT INTO Repairs (StartDate, CarID, RepairType, OneHourPrice, Discount, Hours) VALUES
        ('2023-01-01', 1, 'Type1', 50.00, 0.10, 8.0),
        ('2023-02-01', 2, 'Type2', 60.00, 0.15, 10.0),
        ('2023-03-01', 3, 'Type2', 65.00, 0.15, 10.0),
        ('2023-04-01', 4, 'Type3', 55.00, 0.12, 9.0),
        ('2023-05-01', 1, 'Type4', 70.00, 0.20, 12.0),
        ('2023-06-01', 2, 'Type1', 50.00, 0.10, 8.0),
        ('2023-07-01', 3, 'Type2', 60.00, 0.15, 10.0),
        ('2023-08-01', 4, 'Type3', 55.00, 0.12, 9.0),
        ('2023-09-01', 1, 'Type4', 70.00, 0.20, 12.0),
        ('2023-10-01', 2, 'Type1', 50.00, 0.10, 8.0),
        ('2023-11-01', 3, 'Type2', 60.00, 0.15, 10.0),
        ('2023-12-01', 4, 'Type3', 55.00, 0.12, 9.0),
        ('2024-01-01', 1, 'Type4', 70.00, 0.20, 12.0),
        ('2024-02-01', 2, 'Type1', 50.00, 0.10, 8.0),
        ('2024-03-01', 3, 'Type2', 60.00, 0.15, 10.0);
        """

    cursor.execute(fill_clients_table_query)
    print(f"Fill clients table. Rows affected: {cursor.rowcount}")
    cursor.execute(fill_cars_table_query)
    print(f"Fill cars table. Rows affected: {cursor.rowcount}")
    cursor.execute(fill_repairs_table_query)
    print(f"Fill repairs table. Rows affected: {cursor.rowcount}")

    connection.commit()
    cursor.close()
