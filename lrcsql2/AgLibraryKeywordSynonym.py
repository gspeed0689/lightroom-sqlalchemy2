from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryKeywordSynonym(Base):
	__tablename__ = "AgLibraryKeywordSynonym"
	id_local: Mapped[] = mapped_column(primary_key=True)
	keyword: Mapped[] = mapped_column(nullable=False)
	lc_name: Mapped[] = mapped_column()
	name: Mapped[] = mapped_column()
