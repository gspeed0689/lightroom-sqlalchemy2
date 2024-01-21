from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class MigratedInfo(Base):
	__tablename__ = "MigratedInfo"
	ozCatalogId: Mapped[] = mapped_column(primary_key=True)
	migrationStatus: Mapped[] = mapped_column(nullable=False)
	timestamp: Mapped[] = mapped_column(nullable=False)
