from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_namedIdentityPlate(Base):
	__tablename__ = "Adobe_namedIdentityPlate"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	description: Mapped[] = mapped_column()
	identityPlate: Mapped[] = mapped_column()
	identityPlateHash: Mapped[] = mapped_column()
	moduleFont: Mapped[] = mapped_column()
	moduleSelectedTextColor: Mapped[] = mapped_column()
	moduleTextColor: Mapped[] = mapped_column()
