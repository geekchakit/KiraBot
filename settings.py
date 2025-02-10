from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str = ""
    mongo_url: str = ""

    class Config:
        env_file = ".env"
        extra = "ignore"