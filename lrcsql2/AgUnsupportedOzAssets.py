from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgUnsupportedOzAssets(Base):
	__tablename__ = "AgUnsupportedOzAssets"
	id_local: Mapped[] = mapped_column(primary_key=True)
	ozAssetId: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	path: Mapped[] = mapped_column(nullable=False)
	type: Mapped[] = mapped_column(nullable=False)
	payload: Mapped[] = mapped_column(nullable=False)
