from database import DatabaseManager

def setup():
    db_manager = DatabaseManager()
    db_manager.create_database()

setup()