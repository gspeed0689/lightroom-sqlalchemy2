from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_libraryImageDevelopSnapshot(Base):
	__tablename__ = "Adobe_libraryImageDevelopSnapshot"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	digest: Mapped[] = mapped_column()
	hasBigData: Mapped[] = mapped_column(nullable=False)
	hasDevelopAdjustments: Mapped[] = mapped_column()
	image: Mapped[] = mapped_column()
	locked: Mapped[] = mapped_column()
	name: Mapped[] = mapped_column()
	snapshotID: Mapped[] = mapped_column()
	text: Mapped[] = mapped_column()
