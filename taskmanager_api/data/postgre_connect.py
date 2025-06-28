from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel

class Base(DeclarativeBase): pass
        

class PostgreConfig(BaseModel):
    host: str
    port: str
    username: str
    password: str
    db_name: str
    
    def get_url(self) -> str:
        return f"postgresql+asynpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"
    

class PostgreConnect:
    def __init__(self, config: PostgreConfig):
        self.config = config
        self.engine = create_async_engine(self.config.get_url(), echo=True)
        self.sessionmaker = async_sessionmaker(self.engine, expire_on_commit=False)
        
        
    def get_session(self) -> AsyncSession:
        return self.sessionmaker()

    
    async def init_db(self):
        async with self.engine.begin() as con:
            await con.run_sync(Base.metadata.create_all)