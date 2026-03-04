import os

class Config:
    SECRET_KEY = "replace-with-secure-key"
    DEBUG = False
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

class DevelopmentConfig(Config):
    DEBUG = True
