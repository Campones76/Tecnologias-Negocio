DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'NEUROX21-LAPTOP' #  SERVER_NAME = ''
DATABASE_NAME = 'ItOnDemand' 
UID = 'ten2' # UID = 'teste2'
PWD = '1234'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    PWD={PWD};
    UID={UID};
    Trust_Connection=yes;
"""
