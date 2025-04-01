from flask import Flask
from config import app
from flask_cors import CORS
import routes

if __name__ == "__main__":
    app.run(debug=True)