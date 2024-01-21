from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryCollectionSyncedAlbumData(Base):
	__tablename__ = "AgLibraryCollectionSyncedAlbumData"
	collection: Mapped[] = mapped_column(nullable=False)
	payloadKey: Mapped[] = mapped_column(nullable=False)
	payloadData: Mapped[] = mapped_column(nullable=False)
