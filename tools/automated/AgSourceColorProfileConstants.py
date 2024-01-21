from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgSourceColorProfileConstants(Base):
	__tablename__ = "AgSourceColorProfileConstants"
	id_local: Mapped[] = mapped_column(primary_key=True)
	image: Mapped[] = mapped_column(nullable=False)
	profileName: Mapped[] = mapped_column(nullable=False)
