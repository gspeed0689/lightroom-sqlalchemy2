from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class MigratedCollectionImages(Base):
	__tablename__ = "MigratedCollectionImages"
	ozAlbumId: Mapped[] = mapped_column(nullable=False)
	ozAlbumAssetId: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	localCollectionId: Mapped[] = mapped_column(nullable=False)
	localCollectionImageId: Mapped[] = mapped_column(nullable=False)
	UNIQUE: Mapped[] = mapped_column(unique=True)
