from dotenv import load_dotenv
from os import getenv
import psycopg2

load_dotenv()

class PGSQL:
    __user = getenv('USER')
    __password = getenv('PASSWORD')
    __server = getenv('SERVER')
    
    __pg_con = psycopg2.connect(
        dbname = __user,
        user = __user,
        password = __password,
        host = __server
    )
    
    __cur = __pg_con.cursor()
    
    def create_tables(self, sql_filepath:str):
        start = self.create_file(sql_filepath)
        
        tables = start.split(';')
        
        for table in tables:
            try:
                print(table)
                self.__cur.execute(table)
                self.__pg_con.commit()
            except psycopg2.ProgrammingError as msg:
                print(f'Command Skipped: {msg}')
    def insert_data(self, sql_filepath:str):
        start = self.create_file(sql_filepath)
        data_to_insert = start.split(';')
        for insert in data_to_insert:
            try:
                print(insert)
                self.__cur.execute(insert)
                self.__pg_con.commit()
            except psycopg2.ProgrammingError as msg:
                print(f'Command Skipped: {msg}\n {insert}')
                
    @staticmethod
    def create_file(filepath:str):
        '''Opens a file by the filepath and apply it to a SQL Server'''
        with open(filepath, 'r') as f:
            sql_file = f.read()
        return sql_file
    
if __name__ == '__main__':
    c = PGSQL()
    c.create_tables(r'sql-test/amazon_mock_create.sql')
    c.insert_data(r'sql-test/amazon_mock_insert.sql')