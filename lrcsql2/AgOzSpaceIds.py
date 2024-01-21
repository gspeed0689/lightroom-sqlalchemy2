from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgOzSpaceIds(Base):
	__tablename__ = "AgOzSpaceIds"
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	ozSpaceId: Mapped[] = mapped_column(nullable=False)
