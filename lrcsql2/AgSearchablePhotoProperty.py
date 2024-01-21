from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgSearchablePhotoProperty(Base):
	__tablename__ = "AgSearchablePhotoProperty"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	dataType: Mapped[] = mapped_column()
	internalValue: Mapped[] = mapped_column()
	lc_idx_internalValue: Mapped[] = mapped_column()
	photo: Mapped[] = mapped_column(nullable=False)
	propertySpec: Mapped[] = mapped_column(nullable=False)
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	arrayIndex: Mapped[] = mapped_column(nullable=False)
	dataType: Mapped[] = mapped_column()
	internalValue: Mapped[] = mapped_column()
	lc_idx_internalValue: Mapped[] = mapped_column()
	photo: Mapped[] = mapped_column(nullable=False)
	propertySpec: Mapped[] = mapped_column(nullable=False)
