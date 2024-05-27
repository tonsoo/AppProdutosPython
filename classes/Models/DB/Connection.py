import pypyodbc 
import pandas as pd

class Connection:

    def __init__(self, username, password, database = '', server = 'localhost') -> None:
        if not database:
            database = username
        
        self.conn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        f"Server={server};"
                        f"Database={database};"
                        f"uid={username};pwd={password}")
    
    def execute(self, query:str) -> list:
        self.df = pd.read_sql_query(query, self.conn)
        return []