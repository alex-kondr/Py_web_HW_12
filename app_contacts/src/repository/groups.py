from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.database.models import Group, User
from src.schemas.groups import GroupModel


async def get_groups()