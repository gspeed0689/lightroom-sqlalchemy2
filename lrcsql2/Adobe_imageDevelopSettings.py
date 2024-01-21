from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_imageDevelopSettings(Base):
	__tablename__ = "Adobe_imageDevelopSettings"
	id_local: Mapped[] = mapped_column(primary_key=True)
	allowFastRender: Mapped[] = mapped_column()
	beforeSettingsIDCache: Mapped[] = mapped_column()
	croppedHeight: Mapped[] = mapped_column()
	croppedWidth: Mapped[] = mapped_column()
	digest: Mapped[] = mapped_column()
	fileHeight: Mapped[] = mapped_column()
	fileWidth: Mapped[] = mapped_column()
	grayscale: Mapped[] = mapped_column()
	hasAIMasks: Mapped[] = mapped_column(nullable=False)
	hasBigData: Mapped[] = mapped_column(nullable=False)
	hasDevelopAdjustments: Mapped[] = mapped_column()
	hasDevelopAdjustmentsEx: Mapped[] = mapped_column()
	hasLensBlur: Mapped[] = mapped_column(nullable=False)
	hasMasks: Mapped[] = mapped_column(nullable=False)
	hasRetouch: Mapped[] = mapped_column()
	historySettingsID: Mapped[] = mapped_column()
	image: Mapped[] = mapped_column()
	isHdrEditMode: Mapped[] = mapped_column(nullable=False)
	processVersion: Mapped[] = mapped_column()
	profileCorrections: Mapped[] = mapped_column()
	removeChromaticAberration: Mapped[] = mapped_column()
	settingsID: Mapped[] = mapped_column()
	snapshotID: Mapped[] = mapped_column()
	text: Mapped[] = mapped_column()
	validatedForVersion: Mapped[] = mapped_column()
	whiteBalance: Mapped[] = mapped_column()
