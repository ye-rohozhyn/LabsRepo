import os
import pymysql.cursors
from prettytable import PrettyTable


def execute_and_display_query(query, connection):
    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]

            result_table = PrettyTable(columns)
            result_table.align = 'l'

            for row in cursor.fetchall():
                result_table.add_row(row)

            print("\nQuery Result:")
            print(result_table)

        except Exception as e:
            print(f"An error occurred: {str(e)}")


connection = pymysql.connect(db='ford_db', user='admin', passwd='admin', host='localhost', port=3333)

queries_dir = 'Queries'

for filename in os.listdir(queries_dir):
    if filename.endswith(".sql"):
        filepath = os.path.join(queries_dir, filename)

        with open(filepath, 'r') as file:
            query = file.read()

        print(f"\nExecuting query from {filename}:")
        execute_and_display_query(query, connection)

connection.close()
