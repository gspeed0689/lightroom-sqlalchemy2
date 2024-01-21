from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_AdditionalMetadata(Base):
	__tablename__ = "Adobe_AdditionalMetadata"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	additionalInfoSet: Mapped[] = mapped_column(nullable=False)
	embeddedXmp: Mapped[] = mapped_column(nullable=False)
	externalXmpIsDirty: Mapped[] = mapped_column(nullable=False)
	image: Mapped[] = mapped_column()
	incrementalWhiteBalance: Mapped[] = mapped_column(nullable=False)
	internalXmpDigest: Mapped[] = mapped_column()
	isRawFile: Mapped[] = mapped_column(nullable=False)
	lastSynchronizedHash: Mapped[] = mapped_column()
	lastSynchronizedTimestamp: Mapped[] = mapped_column(nullable=False)
	metadataPresetID: Mapped[] = mapped_column()
	metadataVersion: Mapped[] = mapped_column()
	monochrome: Mapped[] = mapped_column(nullable=False)
	xmp: Mapped[] = mapped_column(nullable=False)
