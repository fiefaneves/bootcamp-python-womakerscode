from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_PORT: int
    DATABASE_PASSWORD: str
    DATABASE_USER: str
    DATABASE_DB: str
    DATABASE_HOST: str
    DATABASE_HOSTNAME: str
    
    class Config:
        env_file = './.env'

settings = Settings()        