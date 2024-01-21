from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryKeywordPopularity(Base):
	__tablename__ = "AgLibraryKeywordPopularity"
	id_local: Mapped[] = mapped_column(primary_key=True)
	occurrences: Mapped[] = mapped_column(nullable=False)
	popularity: Mapped[] = mapped_column(nullable=False)
	tag: Mapped[] = mapped_column(nullable=False, unique=True)
