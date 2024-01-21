from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgPendingOzAuxBinaryDownloads(Base):
	__tablename__ = "AgPendingOzAuxBinaryDownloads"
	auxId: Mapped[] = mapped_column(nullable=False)
	ozAssetId: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	payloadHash: Mapped[] = mapped_column(nullable=False)
	whenQueued: Mapped[] = mapped_column(nullable=False)
	state: Mapped[] = mapped_column(nullable=False)
