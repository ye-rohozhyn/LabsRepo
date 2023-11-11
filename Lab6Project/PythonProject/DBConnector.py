import pymysql.cursors
from prettytable import PrettyTable

connection = pymysql.connect(db='ford_db', user='admin', passwd='admin', host='localhost', port=3333)


def display_table_structure(table_name):
    with connection.cursor() as cursor:
        try:
            cursor.execute(f"DESCRIBE {table_name}")
            structure_columns = [desc[0] for desc in cursor.description]

            structure_table = PrettyTable(structure_columns)
            structure_table.align = 'l'
            structure_table.add_row(cursor.fetchone())
            for row in cursor.fetchall():
                structure_table.add_row(row)

            print(f"\nTable: {table_name}")
            print("\nStructure:")
            print(structure_table)

        except Exception as e:
            print(f"An error occurred: {str(e)}")


def display_table_data(table_name):
    with connection.cursor() as cursor:
        try:
            cursor.execute(f"SELECT * FROM {table_name}")

            data_columns = [desc[0] for desc in cursor.description]
            data_table = PrettyTable(data_columns)
            data_table.align = 'l'
            for row in cursor.fetchall():
                if any(row):
                    data_table.add_row(row)

            print(f"\nTable: {table_name}")
            print("\nData:")
            print(data_table)

        except Exception as e:
            print(f"An error occurred: {str(e)}")


with connection.cursor() as cursor:
    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor.fetchall()]

print("Available Tables:")
for idx, table in enumerate(tables, start=1):
    print(f"{idx}. {table}")

while True:
    try:
        choice = int(input("Enter the number of the table you want to view (0 to exit): "))
        if choice == 0:
            break
        elif 1 <= choice <= len(tables):
            selected_table = tables[choice - 1]
            display_table_structure(selected_table)
            display_table_data(selected_table)
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")
        break

connection.close()
