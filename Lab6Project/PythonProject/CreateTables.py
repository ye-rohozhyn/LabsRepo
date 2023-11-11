import pymysql.cursors

connection = pymysql.connect(db='ford_db', user='admin', passwd='admin', host='localhost', port=3333)


def try_execute_query(query: str):
    try:
        cursor.execute(query)
        connection.commit()
        print("Query execute successful!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


with connection:
    cursor = connection.cursor()

    create_clients_table_query = """
        CREATE TABLE IF NOT EXISTS Clients (
            ClientID INT AUTO_INCREMENT PRIMARY KEY,
            ClientCompany VARCHAR(255),
            CheckingAccount VARCHAR(255),
            PhoneNumber VARCHAR(15),
            ContactPerson VARCHAR(255),
            Address VARCHAR(255)
        )
        """
    create_cars_table_query = """
    CREATE TABLE IF NOT EXISTS Cars (
        CarID INT AUTO_INCREMENT PRIMARY KEY,
        CarBrand VARCHAR(255),
        CarPrice DECIMAL(10, 2),
        ClientID INT,
        FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
    )
    """
    create_repairs_table_query = """
    CREATE TABLE IF NOT EXISTS Repairs (
        RepairID INT AUTO_INCREMENT PRIMARY KEY,
        StartDate DATE,
        CarID INT,
        RepairType VARCHAR(255),
        OneHourPrice DECIMAL(10, 2),
        Discount DECIMAL(4, 2),
        Hours DECIMAL(6, 2),
        FOREIGN KEY (CarID) REFERENCES Cars(CarID)
    )
    """

    try_execute_query(create_clients_table_query)
    try_execute_query(create_cars_table_query)
    try_execute_query(create_repairs_table_query)

    cursor.close()