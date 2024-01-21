from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryImageChangeCounter(Base):
	__tablename__ = "AgLibraryImageChangeCounter"
	image: Mapped[] = mapped_column(primary_key=True)
	changeCounter: Mapped[] = mapped_column()
	changedAtTime: Mapped[] = mapped_column()
	localTimeOffsetSecs: Mapped[] = mapped_column()
