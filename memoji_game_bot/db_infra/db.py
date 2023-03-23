from datetime import datetime
from typing import Optional

from aiocache import cached
from aiocache.serializers import PickleSerializer
from loguru import logger

from memoji_game_bot.db_infra.models import conn, Users


@cached(ttl=0.2, serializer=PickleSerializer())
async def check_user_registered(user_social_id: int):
    user = await get_user(user_social_id)
    logger.info(f"Checked user db id = {user}, registration is {bool(user)}")
    return bool(user)


async def get_user(user_social_id: int) -> Optional[Users]:
    try:
        user = await conn.get(Users, social_id=user_social_id)
        return user
    except Exception:
        return None


async def create_user(*, user_social_id: int, username: str):
    await conn.create(Users, social_id=user_social_id, username=username, registration_date=datetime.now())
    logger.info(f"New user[{username}] registered")
