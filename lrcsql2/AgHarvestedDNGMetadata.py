from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgHarvestedDNGMetadata(Base):
	__tablename__ = "AgHarvestedDNGMetadata"
	id_local: Mapped[] = mapped_column(primary_key=True)
	image: Mapped[] = mapped_column()
	hasFastLoadData: Mapped[] = mapped_column()
	hasLossyCompression: Mapped[] = mapped_column()
	isDNG: Mapped[] = mapped_column()
	isHDR: Mapped[] = mapped_column()
	isPano: Mapped[] = mapped_column()
	isReducedResolution: Mapped[] = mapped_column()
