from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    TEST_DATABASE_URL: str
    APP_ENV: str = 'dev'

    class Config:
        env_file = '.env'

settings = Settings()
