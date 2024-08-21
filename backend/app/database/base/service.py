from typing import Optional
from sqlmodel.ext.asyncio.session import AsyncSession


class BaseService:
    """
    Base Service

    Attributes:

        db_session (AsyncSession): database session
    """

    db_session: Optional[AsyncSession]
    domain: Optional[str]

    def __init__(self, db_session: AsyncSession, domain: Optional[str] = None):
        self.db_session = db_session
        self.domain = domain
