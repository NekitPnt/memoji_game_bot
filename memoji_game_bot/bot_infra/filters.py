from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from memoji_game_bot.config import settings
from memoji_game_bot.db_infra.db import check_user_registered


class AbsFilter(BoundFilter):
    key = "key"

    def __init__(self, **kwargs):
        setattr(self, self.key, kwargs[self.key])

    async def check(self, msg: types.Message):
        return True


class CreatorFilter(AbsFilter):
    key = "creator"

    async def check(self, msg: types.Message):
        return settings.creator_id is None or str(msg.from_user.id) == settings.creator_id


class RegistrationFilter(AbsFilter):
    key = "registered"

    async def check(self, msg: types.Message):
        return await check_user_registered(msg.from_user.id)


class NonRegistrationFilter(AbsFilter):
    key = "not_registered"

    async def check(self, msg: types.Message):
        return not await check_user_registered(msg.from_user.id)
