from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB, 

from datetime import datetime

class Adobe_AdditionalMetadata(Base):
	__tablename__ = "Adobe_AdditionalMetadata"
	id_local: Mapped[int] = mapped_column(Integer, primary_key=True)
	id_global: Mapped[str] = mapped_column(Uuid, nullable=False, unique=True)
	additionalInfoSet: Mapped[int] = mapped_column(nullable=False)
	embeddedXmp: Mapped[int] = mapped_column(nullable=False)
	externalXmpIsDirty: Mapped[int] = mapped_column(nullable=False)
	image: Mapped[int] = mapped_column()
	incrementalWhiteBalance: Mapped[int] = mapped_column(nullable=False)
	internalXmpDigest: Mapped[] = mapped_column()
	isRawFile: Mapped[] = mapped_column(nullable=False)
	lastSynchronizedHash: Mapped[] = mapped_column()
	lastSynchronizedTimestamp: Mapped[] = mapped_column(nullable=False)
	metadataPresetID: Mapped[] = mapped_column()
	metadataVersion: Mapped[] = mapped_column()
	monochrome: Mapped[] = mapped_column(nullable=False)
	xmp: Mapped[] = mapped_column(nullable=False)
