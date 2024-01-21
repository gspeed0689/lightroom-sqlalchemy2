from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgSearchablePhotoPropertyArrayElement(Base):
	__tablename__ = "AgSearchablePhotoPropertyArrayElement"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	arrayIndex: Mapped[] = mapped_column(nullable=False)
	dataType: Mapped[] = mapped_column()
	internalValue: Mapped[] = mapped_column()
	lc_idx_internalValue: Mapped[] = mapped_column()
	photo: Mapped[] = mapped_column(nullable=False)
	propertySpec: Mapped[] = mapped_column(nullable=False)
