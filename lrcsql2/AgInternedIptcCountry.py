from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgInternedIptcCountry(Base):
	__tablename__ = "AgInternedIptcCountry"
	id_local: Mapped[] = mapped_column(primary_key=True)
	searchIndex: Mapped[] = mapped_column()
	value: Mapped[] = mapped_column()
