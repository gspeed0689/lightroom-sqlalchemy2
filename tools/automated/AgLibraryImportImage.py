from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryImportImage(Base):
	__tablename__ = "AgLibraryImportImage"
	id_local: Mapped[] = mapped_column(primary_key=True)
	image: Mapped[] = mapped_column(nullable=False)
	import: Mapped[] = mapped_column(nullable=False)
