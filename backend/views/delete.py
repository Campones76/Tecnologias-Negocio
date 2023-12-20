import time
import pandas as pd
import configparser
import openpyxl
import re
import os
import mysql.connector
import mysql.connector.pooling
# Config File Location
config_location = 'ExcelData\\Config\\config.conf' #Config Location Gabriel Windows
#config_location = '/Users/School/Documents/GitHub/Trabalho-Processamento-de-Dados/ExcelData/Config/config.conf' #Config Location Gabriel MacOS
#directory = '\\mac\Home\Documents\GitHub\Trabalho-Processamento-de-Dados\Dataset\dataset\\'
# Initialization of the config file
def init_config():
    # Create a config parser
    config = configparser.ConfigParser()
    config.read(config_location)
    return config['CONFIG']


# Initialize the config
config = init_config()

# Get the output file location from the config
output = config['OUTPUT']
# Get the search value from the config
search_value = config['SEARCH_VALUE']

# Get the directory name from the config
directory_name = config['DIRECTORY']
# Isto está um pouco ás 3 pancadas vai ser para refazermos visto que está basicamente tudo hardcoded temos que ver se conseguimos meter isto numa maneira mais dinâmica 27/10/2023
# row1 = config['ROW1']
# row2 = config['ROW2']
# row3 = config['ROW3']
# row4 = config['ROW4']
# row5 = config['ROW5']
# row6 = config['ROW6']
# row7 = config['ROW7']
# row8 = config['ROW8']
# row9 = config['ROW9']
# row10 = config['ROW10']
# row11 = config['ROW11']
# row12 = config['ROW12']
# row13 = config['ROW13']
db = config['MYSQL_DATABASE']
db_host = config['MYSQL_HOST']
db_user = config['MYSQL_USER']


db_config = {
        'host': 'localhost',
        'user': 'root',
        'database': 'ertdb'
    }
# Create a connection pool
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="ERTDB_pool",
    pool_size=20,
    **db_config
)


# Function to display the names of all folders in a directory
def display_folders(directory_name):
    try:
        # Gets the names of all folders in the directory
        folders = [folder for folder in sorted(os.listdir(directory_name)) if os.path.isdir(os.path.join(directory_name, folder))]
        # Print the names of every folder
        for i, folder in enumerate(folders, start=1):
            print(f"{i}. {folder}")
        # Return the names of every folder
        return folders
    except FileNotFoundError:
        # Prints a message if the directory isn't found
        print("Directory not found")
        return []
    
# Function to display the names of all sheets in an Excel file
def display_excel_sheets(input_file):
    # Load the SELECTED Excel file
    xls = pd.ExcelFile(input_file)
    # Get the names of all sheets
    sheet_names = xls.sheet_names  # Gets all sheet names
    # Print the names of all sheets
    for i, sheet in enumerate(sheet_names, start=1):
        print(f"{i}. {sheet}")
    # Return the names of all sheets
    return sheet_names

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

# Function to display the names of all columns in a sheet of an Excel file
def display_excel_columns(input_file, sheet_name):
    # Load the sheet from the Excel file
    df_columns = pd.read_excel(input_file, sheet_name, engine='openpyxl')
    
    # Get the names of all columns
    columns = df_columns.columns.tolist()  # Gets all column names
    # Print the names of all columns
    for i, column in enumerate(columns, start=1):
        print(f"{i}. {column}")
    # Return the names of all columns
    return columns

def find_year_in_sheet(excel_file_path, sheet_name, column_index):
    wb = openpyxl.load_workbook(excel_file_path)
    sheet = wb[sheet_name]

    for row in sheet.rows:
        cell = row[column_index]
        values = cell.value

        if values is not None:
            return values

    return None

# Function to read an Excel file and write to an XML file

def read_and_write(input_file, sheet_name):
    global search_value
    # Creates the dataframe
    df_reader = pd.read_excel(input_file, sheet_name, engine='openpyxl')
    # Retrieve the values from the "Capa" sheet
    year = find_year_in_sheet(input_file, "Capa", 2)
    year = re.sub('[qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNMãúóí!@#$/-]', '', year)
    year = re.sub(r"\s+", "", year)
    year = year.replace("–", "")
    print(year)
    # Append the values from the "Capa" sheet to the dataframe
    if year:
       df_reader["Year"] = year

    # Replace spaces and special characters in column names to make XML happy :D <-- That's XML, he's happy
    df_reader.columns = df_reader.columns.str.replace(' ', '_')
    df_reader.columns = df_reader.columns.str.replace('\W', '')
    df_reader.columns = df_reader.columns.str.replace('/', '')
    df_reader.columns = df_reader.columns.str.replace('(', '')
    df_reader.columns = df_reader.columns.str.replace(')', '')
    df_reader.columns = df_reader.columns.str.replace('á', 'a')
    df_reader.columns = df_reader.columns.str.replace('à', 'a')
    df_reader.columns = df_reader.columns.str.replace('ç', 'c')
    df_reader.columns = df_reader.columns.str.replace('ã', 'a')
    df_reader.columns = df_reader.columns.str.replace('í', 'i')
    df_reader.columns = df_reader.columns.str.replace('ì', 'i')
    df_reader.columns = df_reader.columns.str.replace('ú', 'u')
    df_reader.columns = df_reader.columns.str.replace('é', 'e')
    df_reader.columns = df_reader.columns.str.replace('è', 'e')
    df_reader.columns = df_reader.columns.str.replace('ê', 'e')
    df_reader.columns = df_reader.columns.str.replace('%', 'Percentagem')
    df_reader.columns = df_reader.columns.str.replace('º', '_')
    df_reader.columns = df_reader.columns.str.replace('ó', 'o')
    df_reader.columns = df_reader.columns.str.replace('ò', 'o')
    df_reader.columns = df_reader.columns.str.replace('õ', 'o')
    df_reader.columns = df_reader.columns.str.replace(',', '')
    # Gabriel Fernando 2023

    # If no search value is specified, write all data to the XML file

    df_reader.to_xml(output, root_name='Data', row_name='Row', index=False)
    print(f"All data has been saved to {output}.")
    df_reader=pd.DataFrame()
# Function to display the names of all files in a directory
def display_directory_files(directory_name):
    try:
        # Gets the names of all files in the directory in a sorted way
        files = sorted(os.listdir(directory_name))
        # Print the names of every files
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        # Return the names of every files
        return files
    except FileNotFoundError:
        # Prints a message if the directory isn't found
        print("Directory not found")
        return []

#Menu functions
def choose_folder(directory_name):
    print("\n\n\n\n\n\n\n\n\n\n----Directory----")
    folders = display_folders(directory_name)
    
    folder_choice = int(input("Enter the number of the folder you want to select: "))
    if 1 <= folder_choice <= len(folders):
        selected_folder = os.path.join(directory_name, folders[folder_choice - 1])
        print(f"\n\n\n\n\n\n\n\n\n\n----{selected_folder}----")
        files = display_directory_files(selected_folder)
        return selected_folder, files
    else:
        print("\n\n\n\n\n\n\n\n\n\n")
        print("Invalid folder. Please enter a number between 1 and {}.".format(len(folders)))
        return None, None

def choose_file(selected_folder, files):
    global table_name
    file_choice = int(input("Enter the number of the file you want to select: "))
    if 1 <= file_choice <= len(files):
        input_file = os.path.join(selected_folder, files[file_choice - 1])
        print(f"You selected {input_file}")
        print(f"\n\n\n\n\n\n\n\n\n\n\n----{input_file}----")
        # É um horror? sim mas funciona e isso é o que importa :3
        if "ListasRebides" in selected_folder:
            table_name = "ListasRebides"
        elif "ListasPublicaRebides" in selected_folder:
            table_name = "ListasPublicaRebides"
        elif "ListasECDES" in selected_folder:
            table_name = "ListasECDES"
        elif "ListasDocentes" in selected_folder:
            table_name = "ListasDocente"
        else:
            raise ValueError("Nome de arquivo não reconhecido. Certifique-se de que o arquivo está na ListaRebides ou ListaDocentes.")
        return input_file
    else:
        print("\n\n\n\n\n\n\n\n\n\n")
        print("Invalid file choice. Please enter a number between 1 and {}.".format(len(files)))
        return None

def choose_sheet(input_file):
    sheet_names = display_excel_sheets(input_file)
    sheet_choice = int(input("Enter the number of the sheet you want to select: "))
    if 1 <= sheet_choice <= len(sheet_names):
        sheet_name = sheet_names[sheet_choice - 1]
        print(f"You selected {sheet_name}")
        return sheet_name
    if 0 <= sheet_choice:
        choose_file()
    else:
        print("Invalid sheet choice. Please enter a number between 1 and {}.".format(len(sheet_names)))
        return None
#######
while True:
    # Print the menu
    print("\n\n\n\n\n\n\n----Menu----")
    print("1. Choose a folder")
    print("2. Credits")
    print("3. Exit")

    choice = input("Enter your choice: ")
    print("\n\n\n\n\n\n\n\n\n\n")



    # If the user chooses to select a folder
    if choice == '1':
        selected_folder, files = choose_folder(directory_name)
        if selected_folder and files:
            input_file = choose_file(selected_folder, files)
            if input_file:
                sheet_name = choose_sheet(input_file)
                if sheet_name:
                    read_and_write(input_file, sheet_name)
                    print("Do you want to send the output data to the database?\n 1. Yes\n 2. No")
                    mysql_choice = input("Enter the number of the option you want to select: ")
                    if mysql_choice == '1':
                        df_mysql = pd.read_xml(output)
                        mysql_stuff(connection_pool, df_mysql)
                        print("Data Commited to DB")
                    elif mysql_choice == '2':
                        break
                    else:
                        print("\n\n\n\n\n\n\n\n\n\n")
                        print("Invalid choice. Please enter a number between 1 and 2")
    elif choice == '2':
        print("\n----Credits----\nThis project was made by the following students:\n º Gabriel Fernando - 2021101890\n º Gilherme Sousa - 2020101204\n º Rafael Duarte - 2021103639\n")
        input("+----------------------------------------+\n| Press enter to exit to the main screen |\n+----------------------------------------+")
        print("\n\n\n\n\n\n\n\n\n\n")
    elif choice == '3':
        print("Program Exited")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")