from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryFaceData(Base):
	__tablename__ = "AgLibraryFaceData"
	id_local: Mapped[] = mapped_column(primary_key=True)
	data: Mapped[] = mapped_column()
	face: Mapped[] = mapped_column(nullable=False)
