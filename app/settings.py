from pydantic_settings import BaseSettings
from pydantic import BaseModel

class ServerConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 5000
    reload: bool = True
    

class DatabaseConfig(BaseModel):
    url: str = "sqlite:///db.sqlite3"

class Settings(BaseSettings):
    server: ServerConfig = ServerConfig()
    database: DatabaseConfig = DatabaseConfig()


settings: Settings = Settings(
    _env_file=".env", 
    _env_file_encoding="utf-8"
)
