from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_libraryImageFaceProcessHistory(Base):
	__tablename__ = "Adobe_libraryImageFaceProcessHistory"
	id_local: Mapped[] = mapped_column(primary_key=True)
	image: Mapped[] = mapped_column(nullable=False)
	lastFaceDetector: Mapped[] = mapped_column()
	lastFaceRecognizer: Mapped[] = mapped_column()
	lastImageIndexer: Mapped[] = mapped_column()
	lastImageOrientation: Mapped[] = mapped_column()
	lastTryStatus: Mapped[] = mapped_column()
	userTouched: Mapped[] = mapped_column()
