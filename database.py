import sqlite3


class BJ_users:
    """Class for working with the users table"""

    def __init__(self, name):
        self.name = name
        self.con = sqlite3.connect('users.db')
        self.cursor = self.con.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users 
            (name TEXT)
        """)
        self.con.commit()
        
    def create(self):
        """Inserts a new user with the given name into the users table"""
        self.cursor.execute("""INSERT INTO users (name) VALUES (?)""", (self.name,))
        self.con.commit()

    def check_user(self):
        """Checks if a user with the given name already exists in the users table, 
        and creates a new user if not."""
        self.cursor.execute("""SELECT * FROM users WHERE name=?""", (self.name,))
        if self.cursor.fetchone() is None:
            print('You are a new user!!! We saved you')
            BJ_users.create(self)
        else:
            print('Welcome back')


class BJ_dashboard:
    """Class for working with the dashboard table"""

    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score
        self.con = sqlite3.connect('dashboard.db')
        self.cursor = self.con.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS dashboard 
            (name TEXT,
            score INTEGER)
        """)
        self.con.commit()

    def add_user_score(self):
        """Adds a new user with the given name and score to the dashboard table"""
        self.cursor.execute("""INSERT INTO dashboard (name, score) VALUES (?, ?)""", (self.name, self.score,))
        print('User added to dashboard')
        self.con.commit()

    def check_dashboard(self):
        """Displays the top 20 users from the dashboard table, sorted by score"""
        self.cursor.execute("""SELECT * FROM dashboard ORDER BY score DESC LIMIT 20""")
        res = self.cursor.fetchall()
        naming = '----DASHBOARD----'
        print(naming)
        for j, i in enumerate(res, 1):
            print(f'{j}. {i[0]} - {i[1]}')
        print(len(naming)*'-')


    def clear_dashboard(self):
        """Deletes all users from the dashboard table"""
        self.cursor.execute("""DELETE FROM dashboard""")
        print('Dashboard was cleared')
        self.con.commit()
