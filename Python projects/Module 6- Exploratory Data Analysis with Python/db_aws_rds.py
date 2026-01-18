import pymysql

#connect to the database
connection = pymysql.connect(
    host='newdb.cvg08ocmuv01.eu-north-1.rds.amazonaws.com',
    user='root',
    password='root1234',
    database='student_management_system',
    cursorclass= pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            department VARCHAR(255)
        );
        """
        cursor.execute(create_table_query)
        
        # inserting data into the table
        insert_data_query = """
        INSERT INTO students (name, department) VALUES ('Raghul', 'Computer Science');
        """
        cursor.execute(insert_data_query)
        connection.commit()

        # retrieving data from the table
        select_data_query = "SELECT * FROM students;"
        cursor.execute(select_data_query)

        #fetching all the records
        results = cursor.fetchall()
        for row in results:
            print(row)

finally:
    connection.close()