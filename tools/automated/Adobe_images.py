from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_images(Base):
	__tablename__ = "Adobe_images"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	aspectRatioCache: Mapped[] = mapped_column(nullable=False)
	bitDepth: Mapped[] = mapped_column(nullable=False)
	captureTime: Mapped[] = mapped_column()
	colorChannels: Mapped[] = mapped_column(nullable=False)
	colorLabels: Mapped[] = mapped_column(nullable=False)
	colorMode: Mapped[] = mapped_column(nullable=False)
	copyCreationTime: Mapped[] = mapped_column(nullable=False)
	copyName: Mapped[] = mapped_column()
	copyReason: Mapped[] = mapped_column()
	developSettingsIDCache: Mapped[] = mapped_column()
	editLock: Mapped[] = mapped_column(nullable=False)
	fileFormat: Mapped[] = mapped_column(nullable=False)
	fileHeight: Mapped[] = mapped_column()
	fileWidth: Mapped[] = mapped_column()
	hasMissingSidecars: Mapped[] = mapped_column()
	masterImage: Mapped[] = mapped_column()
	orientation: Mapped[] = mapped_column()
	originalCaptureTime: Mapped[] = mapped_column()
	originalRootEntity: Mapped[] = mapped_column()
	panningDistanceH: Mapped[] = mapped_column()
	panningDistanceV: Mapped[] = mapped_column()
	pick: Mapped[] = mapped_column(nullable=False)
	positionInFolder: Mapped[] = mapped_column(nullable=False)
	propertiesCache: Mapped[] = mapped_column()
	pyramidIDCache: Mapped[] = mapped_column()
	rating: Mapped[] = mapped_column()
	rootFile: Mapped[] = mapped_column(nullable=False)
	sidecarStatus: Mapped[] = mapped_column()
	touchCount: Mapped[] = mapped_column(nullable=False)
	touchTime: Mapped[] = mapped_column(nullable=False)
