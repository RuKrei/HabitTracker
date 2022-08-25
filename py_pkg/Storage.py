import sqlite3
class Storage:
    """A class to store and retrieve habit data via SQLite3"""
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_tables()
    
    def connect(self):
        """Connect to the database"""
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        
    def read_all_habits(self):
        """Read all habits from the database"""
        self.cursor.execute("SELECT * FROM habits")
        return self.cursor.fetchall()
    
    def read_one_habit(self, habit_name):
        """Read one habit from the database"""
        self.cursor.execute("SELECT * FROM habits WHERE name = ?", (habit_name,))
        return self.cursor.fetchone()

    def create_tables(self):
        """Create the tables if they don't exist"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY,
            name TEXT,
            periodicity INTEGER,
            timestamp INTEGER,
            type TEXT,
            check_offs TEXT
        )""")
        self.conn.commit()
        
    