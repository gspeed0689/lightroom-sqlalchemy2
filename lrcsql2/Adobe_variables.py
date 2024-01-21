from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class Adobe_variables(Base):
	__tablename__ = "Adobe_variables"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	name: Mapped[] = mapped_column()
	value: Mapped[] = mapped_column()
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	name: Mapped[] = mapped_column()
	type: Mapped[] = mapped_column()
	value: Mapped[] = mapped_column(nullable=False)
