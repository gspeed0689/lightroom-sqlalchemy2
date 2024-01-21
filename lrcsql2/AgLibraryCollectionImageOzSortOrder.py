from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryCollectionImageOzSortOrder(Base):
	__tablename__ = "AgLibraryCollectionImageOzSortOrder"
	collectionImage: Mapped[] = mapped_column(primary_key=True)
	collection: Mapped[] = mapped_column(nullable=False)
	positionInCollection: Mapped[] = mapped_column(nullable=False)
	ozSortOrder: Mapped[] = mapped_column(nullable=False)
