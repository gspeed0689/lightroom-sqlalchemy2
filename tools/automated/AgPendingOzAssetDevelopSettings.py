from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgPendingOzAssetDevelopSettings(Base):
	__tablename__ = "AgPendingOzAssetDevelopSettings"
	ozAssetId: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	payloadHash: Mapped[] = mapped_column(nullable=False)
	developUserUpdated: Mapped[] = mapped_column()
