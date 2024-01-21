from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgOzCorruptedAuxIds(Base):
	__tablename__ = "AgOzCorruptedAuxIds"
	auxId: Mapped[] = mapped_column(nullable=False)
	ozAssetId: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
