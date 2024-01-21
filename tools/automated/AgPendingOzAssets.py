from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgPendingOzAssets(Base):
	__tablename__ = "AgPendingOzAssets"
	ozAssetId: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	state: Mapped[] = mapped_column()
	path: Mapped[] = mapped_column(nullable=False)
	payload: Mapped[] = mapped_column(nullable=False)
