from config import db, app

with app.app_context():
    db.create_all()
    print("Database and tables created successfully!")
