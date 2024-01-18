DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'SCHOOL594B' # Rafa SERVER_NAME = 'LAPTOP-SGU8BV5L'
DATABASE_NAME = 'GunStore' # Guilherme DATABASE_NAME = 'GunStore'
UID = 'GunstoreStaff' # Rafa UID = 'teste1'
PWD = '1234'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    PWD={PWD};
    UID={UID};
    Trust_Connection=yes;
"""
