from app import create_app
from app.config import DevelopmentConfig

app = create_app(DevelopmentConfig)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=app.config.get("DEBUG", False))
