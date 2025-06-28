from redis.asyncio import Redis
from .data.config import PostgreConfig, RedisConfig
from .data.postgre_connect import PostgreConnect
from .data.redis_connect import RedisConnect
from .data.models import Task, User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, insert, delete
from datetime import datetime

class TaskManagerAPI:
    def __init__(self, pg_config: PostgreConfig, redis_config: RedisConfig):
        self.redis = RedisConnect(redis_config)
        self.pg = PostgreConnect(pg_config)
        
        
    def get_pg(self) -> AsyncSession:
        return self.pg
    
    def get_redis(self) -> Redis:
        return self.redis
    
    
    async def get_tasks(self, user_id: int) -> list[Task]:
        async with self.pg.get_session() as session:
            result = await session.scalars(select(Task).where(Task.user_id == user_id))
            return result.all()
        
    async def get_users(self) -> list[User]:
        async with self.pg.get_session() as session:
            result = await session.scalars(select(User))
            return result.all()
        
    async def get_user_info(self, user_id: int) -> User:
        async with self.pg.get_session() as session:
            result = await session.scalar(select(User).where(User.id == user_id))
            return result
        
        
    async def get_task(self, task_id: int) -> Task:
        async with self.pg.get_session() as session:
            result = await session.scalar(select(Task).where(Task.id == task_id))
            return result
        
    
    async def edit_task(self, task_id: int, title: str = None, description: str = None, expire_time: datetime = None) -> None:
        async with self.pg.get_session() as session:
            task = await session.scalar(select(Task).where(Task.id == task_id))
            if task:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                if expire_time is not None:
                    task.expire_time = expire_time
                    
                await session.commit()
                
    async def add_new_user(self, user_id: int, username: str = None, name: str = None) -> None:
        async with self.pg.get_session() as session:
            user = await session.scalar(select(User).where(User.id == user_id))
            if not user:
                await session.execute(insert(User).values(id=user_id, username=username, name=name, referal_link=f"https://t.me/taskmanager_ai_bot?start=ref{user_id}"))
                await session.commit()
                
    