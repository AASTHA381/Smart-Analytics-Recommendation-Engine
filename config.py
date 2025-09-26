import os
from pathlib import Path

class Config:
    """Configuration settings for the application"""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-in-production'
    DEBUG = True
    
    # Data paths
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / 'data'
    
    # ML model settings
    MODEL_CACHE_SIZE = 100
    RECOMMENDATION_LIMIT = 10
    
    # Database settings (if needed in future)
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
