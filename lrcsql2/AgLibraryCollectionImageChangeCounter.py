from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryCollectionImageChangeCounter(Base):
	__tablename__ = "AgLibraryCollectionImageChangeCounter"
	collectionImage: Mapped[] = mapped_column(primary_key=True)
	collection: Mapped[] = mapped_column(nullable=False)
	image: Mapped[] = mapped_column(nullable=False)
	changeCounter: Mapped[] = mapped_column()
