from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgPendingOzAlbumAssetIds(Base):
	__tablename__ = "AgPendingOzAlbumAssetIds"
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	ozAlbumAssetId: Mapped[] = mapped_column(nullable=False)
	ozAssetId: Mapped[] = mapped_column(nullable=False)
	ozAlbumId: Mapped[] = mapped_column(nullable=False)
	ozSortOrder: Mapped[] = mapped_column()
	ozIsCover: Mapped[] = mapped_column()
