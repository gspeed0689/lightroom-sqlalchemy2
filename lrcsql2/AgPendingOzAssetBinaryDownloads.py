from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgPendingOzAssetBinaryDownloads(Base):
	__tablename__ = "AgPendingOzAssetBinaryDownloads"
	ozAssetId: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	whenQueued: Mapped[] = mapped_column(nullable=False)
	path: Mapped[] = mapped_column(nullable=False)
	state: Mapped[] = mapped_column()
