from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_imageProofSettings(Base):
	__tablename__ = "Adobe_imageProofSettings"
	id_local: Mapped[] = mapped_column(primary_key=True)
	colorProfile: Mapped[] = mapped_column()
	image: Mapped[] = mapped_column()
	renderingIntent: Mapped[] = mapped_column()
