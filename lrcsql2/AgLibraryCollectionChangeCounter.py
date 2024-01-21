from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryCollectionChangeCounter(Base):
	__tablename__ = "AgLibraryCollectionChangeCounter"
	collection: Mapped[] = mapped_column(primary_key=True)
	changeCounter: Mapped[] = mapped_column()
