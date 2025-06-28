from .init import TaskManagerAPI
from .data.config import RedisConfig, PostgreConfig

pg_config = PostgreConfig(host="localhost", port="5432", username="postgres", password="pass", db_name="taskmanager_db")
redis_config = RedisConfig(host="localhost", port=6379, db=1)

TaskManagerAPI = TaskManagerAPI(pg_config, redis_config)

__all__ = ["TaskManagerAPI"]