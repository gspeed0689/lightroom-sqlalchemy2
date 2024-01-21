from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgHarvestedExifMetadata(Base):
	__tablename__ = "AgHarvestedExifMetadata"
	id_local: Mapped[] = mapped_column(primary_key=True)
	image: Mapped[] = mapped_column()
	aperture: Mapped[] = mapped_column()
	cameraModelRef: Mapped[] = mapped_column()
	cameraSNRef: Mapped[] = mapped_column()
	dateDay: Mapped[] = mapped_column()
	dateMonth: Mapped[] = mapped_column()
	dateYear: Mapped[] = mapped_column()
	flashFired: Mapped[] = mapped_column()
	focalLength: Mapped[] = mapped_column()
	gpsLatitude: Mapped[] = mapped_column()
	gpsLongitude: Mapped[] = mapped_column()
	gpsSequence: Mapped[] = mapped_column(nullable=False)
	hasGPS: Mapped[] = mapped_column()
	isoSpeedRating: Mapped[] = mapped_column()
	lensRef: Mapped[] = mapped_column()
	shutterSpeed: Mapped[] = mapped_column()
