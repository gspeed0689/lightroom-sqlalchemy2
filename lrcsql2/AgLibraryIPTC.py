from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryIPTC(Base):
	__tablename__ = "AgLibraryIPTC"
	id_local: Mapped[] = mapped_column(primary_key=True)
	caption: Mapped[] = mapped_column()
	copyright: Mapped[] = mapped_column()
	image: Mapped[] = mapped_column(nullable=False)
