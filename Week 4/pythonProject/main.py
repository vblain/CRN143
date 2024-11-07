import psycopg2
from psycopg2 import errors

import configparser # this will import config parser

# create a definition for read the config.ini file and look for 'postgresql' section in file
def get_db_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['postgresql']

try:
    # Connect to an existing database
    db_config = get_db_config() # load the config

    # config loaded and can be used hiding important information
    connection = psycopg2.connect(
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['host'],
        port=db_config['port'],
        database=db_config['database']
    )

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error ) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")