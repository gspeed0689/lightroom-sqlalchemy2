from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_faceProperties(Base):
	__tablename__ = "Adobe_faceProperties"
	id_local: Mapped[] = mapped_column(primary_key=True)
	face: Mapped[] = mapped_column()
	propertiesString: Mapped[] = mapped_column()
