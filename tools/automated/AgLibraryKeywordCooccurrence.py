from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryKeywordCooccurrence(Base):
	__tablename__ = "AgLibraryKeywordCooccurrence"
	id_local: Mapped[] = mapped_column(primary_key=True)
	tag1: Mapped[] = mapped_column(nullable=False)
	tag2: Mapped[] = mapped_column(nullable=False)
	value: Mapped[] = mapped_column(nullable=False)
