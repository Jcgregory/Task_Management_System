from config import db, app  
from sqlalchemy import text  

with app.app_context():  
    with db.engine.connect() as conn:  
        result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))  
        print("Existing tables:", result.fetchall())  