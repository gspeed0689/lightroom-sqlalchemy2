from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryCollectionImage(Base):
	__tablename__ = "AgLibraryCollectionImage"
	id_local: Mapped[] = mapped_column(primary_key=True)
	collection: Mapped[] = mapped_column(nullable=False)
	image: Mapped[] = mapped_column(nullable=False)
	pick: Mapped[] = mapped_column(nullable=False)
	positionInCollection: Mapped[] = mapped_column()
	collectionImage: Mapped[] = mapped_column(primary_key=True)
	collection: Mapped[] = mapped_column(nullable=False)
	image: Mapped[] = mapped_column(nullable=False)
	changeCounter: Mapped[] = mapped_column()
	collectionImage: Mapped[] = mapped_column(nullable=False)
	collection: Mapped[] = mapped_column(nullable=False)
	image: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	ozAlbumAssetId: Mapped[] = mapped_column()
	collectionImage: Mapped[] = mapped_column(primary_key=True)
	collection: Mapped[] = mapped_column(nullable=False)
	positionInCollection: Mapped[] = mapped_column(nullable=False)
	ozSortOrder: Mapped[] = mapped_column(nullable=False)
