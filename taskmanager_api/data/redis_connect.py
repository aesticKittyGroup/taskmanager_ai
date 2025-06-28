from pydantic import BaseModel
from redis.asyncio import Redis
from .config import RedisConfig


class RedisConnect:
    def __init__(self, config: RedisConfig):
        self.config = config
        self.client: Redis | None = None
    
    def connect(self) -> Redis:
        self.client = Redis(host=self.config.host,
                            port=self.config.port,
                            db=self.config.db)
        return self.client