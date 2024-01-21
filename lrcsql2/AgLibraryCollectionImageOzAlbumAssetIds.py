from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryCollectionImageOzAlbumAssetIds(Base):
	__tablename__ = "AgLibraryCollectionImageOzAlbumAssetIds"
	collectionImage: Mapped[] = mapped_column(nullable=False)
	collection: Mapped[] = mapped_column(nullable=False)
	image: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	ozAlbumAssetId: Mapped[] = mapped_column()
