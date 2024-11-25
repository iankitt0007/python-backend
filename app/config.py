from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost/adminPanel"
    JWT_SECRET_KEY: str = "your-secret-key"
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"  # Load variables from .env file
        extra = "allow"  # This allows extra fields like 'secret_key' to be accepted


settings = Settings()
