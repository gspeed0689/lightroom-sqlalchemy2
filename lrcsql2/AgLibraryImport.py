from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryImport(Base):
	__tablename__ = "AgLibraryImport"
	id_local: Mapped[] = mapped_column(primary_key=True)
	imageCount: Mapped[] = mapped_column()
	importDate: Mapped[] = mapped_column(nullable=False)
	name: Mapped[] = mapped_column()
	id_local: Mapped[] = mapped_column(primary_key=True)
	image: Mapped[] = mapped_column(nullable=False)
	import: Mapped[] = mapped_column(nullable=False)
