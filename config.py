from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///./health.db"
    twilio_sid: str = ""
    twilio_token: str = ""
    twilio_from: str = ""

settings = Settings()
