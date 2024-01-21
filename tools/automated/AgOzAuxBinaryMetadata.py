from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgOzAuxBinaryMetadata(Base):
	__tablename__ = "AgOzAuxBinaryMetadata"
	auxId: Mapped[] = mapped_column(nullable=False)
	ozAssetId: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	digest: Mapped[] = mapped_column(nullable=False)
	sha256: Mapped[] = mapped_column(nullable=False)
	fileSize: Mapped[] = mapped_column()
	type: Mapped[] = mapped_column(nullable=False)
