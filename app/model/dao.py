from sqlalchemy import select, and_, func

from app.database import async_session_maker
from app.model.models import iphone_models
from app.service.base import BaseDAO


class ModelsDAO(BaseDAO):
    model = iphone_models

