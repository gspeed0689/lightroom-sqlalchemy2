from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgDeletedOzAlbumAssetIds(Base):
	__tablename__ = "AgDeletedOzAlbumAssetIds"
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	ozAlbumAssetId: Mapped[] = mapped_column(nullable=False)
	changeCounter: Mapped[] = mapped_column()
