from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_imageDevelopBeforeSettings(Base):
	__tablename__ = "Adobe_imageDevelopBeforeSettings"
	id_local: Mapped[] = mapped_column(primary_key=True)
	beforeDigest: Mapped[] = mapped_column()
	beforeHasDevelopAdjustments: Mapped[] = mapped_column()
	beforePresetID: Mapped[] = mapped_column()
	beforeText: Mapped[] = mapped_column()
	developSettings: Mapped[] = mapped_column()
	hasBigData: Mapped[] = mapped_column(nullable=False)
