from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryImageSearchData(Base):
	__tablename__ = "AgLibraryImageSearchData"
	id_local: Mapped[] = mapped_column(primary_key=True)
	featInfo: Mapped[] = mapped_column()
	height: Mapped[] = mapped_column()
	idDesc: Mapped[] = mapped_column()
	idDescCh: Mapped[] = mapped_column()
	image: Mapped[] = mapped_column(nullable=False)
	width: Mapped[] = mapped_column()
