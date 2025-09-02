import os

class Config:
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///instance/peakform.db')
  SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')