from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class MigratedCollections(Base):
	__tablename__ = "MigratedCollections"
	ozAlbumId: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	ozName: Mapped[] = mapped_column(nullable=False)
	localId: Mapped[] = mapped_column(nullable=False)
	UNIQUE: Mapped[] = mapped_column(unique=True)
