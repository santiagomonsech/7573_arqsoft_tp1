"""App Initialization"""
from app import app

if __name__ == "__main__":
    app.run(debug=True, port=6379, host= '0.0.0.0')
    