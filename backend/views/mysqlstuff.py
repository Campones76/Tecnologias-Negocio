
'''
[CONFIG]
DIRECTORY = Dataset/
MYSQL_HOST = localhost
MYSQL_USER = root
MYSQL_PASSWORD = 'Pass-word976!'
MYSQL_DATABASE = ertdb
LOGS = ExcelData/Logs/logs.txt
OUTPUT = ExcelData/Output/output.xml
SEARCH_VALUE = 
'''
def mysql_stuff(connection_pool, df_mysql):
    # Get a connection from the pool
    connection = connection_pool.get_connection()

    # Establish a connection to MySQL

    # Specify the cursorclass as dictionary cursor
    cursor = connection.cursor(dictionary=True)

    try:
        # Insert Data into MySQL
        rows_inserted = 0
        for index, Row in df_mysql.iterrows():
            columns = ", ".join(df_mysql.columns)
            values = ", ".join(["%s"] * len(df_mysql.columns))
            dados = [Row.get(col) if pd.notna(Row.get(col)) else None for col in df_mysql.columns]
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values}) ON DUPLICATE KEY UPDATE {', '.join([f'{col} = VALUES({col})' for col in df_mysql.columns])}"
            print("commit3")
            cursor.execute(sql, tuple(dados))
            rows_inserted += 1
            print("commit1")
            connection.commit()
            print("commit")
    finally:
        cursor.close()
        print("cursor closed")