from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_libraryImageDevelopHistoryStep(Base):
	__tablename__ = "Adobe_libraryImageDevelopHistoryStep"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	dateCreated: Mapped[] = mapped_column()
	digest: Mapped[] = mapped_column()
	hasBigData: Mapped[] = mapped_column(nullable=False)
	hasDevelopAdjustments: Mapped[] = mapped_column()
	image: Mapped[] = mapped_column()
	name: Mapped[] = mapped_column()
	relValueString: Mapped[] = mapped_column()
	text: Mapped[] = mapped_column()
	valueString: Mapped[] = mapped_column()
