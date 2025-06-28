from pydantic import BaseModel

class PostgreConfig(BaseModel):
    host: str
    port: str | int
    username: str
    password: str
    db_name: str
    
    def get_url(self) -> str:
        return f"postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"
    
class RedisConfig(BaseModel):
    host: str
    port: int
    db: int