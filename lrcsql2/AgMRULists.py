from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgMRULists(Base):
	__tablename__ = "AgMRULists"
	id_local: Mapped[] = mapped_column(primary_key=True)
	listID: Mapped[] = mapped_column(nullable=False)
	timestamp: Mapped[] = mapped_column(nullable=False)
	value: Mapped[] = mapped_column(nullable=False)
