from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryCollectionCoverImage(Base):
	__tablename__ = "AgLibraryCollectionCoverImage"
	collection: Mapped[] = mapped_column(primary_key=True)
	collectionImage: Mapped[] = mapped_column(nullable=False)
