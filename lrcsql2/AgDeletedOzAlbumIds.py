from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgDeletedOzAlbumIds(Base):
	__tablename__ = "AgDeletedOzAlbumIds"
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	ozAlbumId: Mapped[] = mapped_column(nullable=False)
	changeCounter: Mapped[] = mapped_column()
