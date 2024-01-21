from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgDeletedOzSpaceIds(Base):
	__tablename__ = "AgDeletedOzSpaceIds"
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	ozSpaceId: Mapped[] = mapped_column(nullable=False)
	changeCounter: Mapped[] = mapped_column()
