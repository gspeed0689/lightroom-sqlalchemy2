from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_libraryImageDevelop3DLUTColorTable(Base):
	__tablename__ = "Adobe_libraryImageDevelop3DLUTColorTable"
	id_local: Mapped[] = mapped_column(primary_key=True)
	LUTFullString: Mapped[] = mapped_column()
	LUTHash: Mapped[] = mapped_column(unique=True)
