from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryFileAssetMetadata(Base):
	__tablename__ = "AgLibraryFileAssetMetadata"
	fileId: Mapped[] = mapped_column(primary_key=True)
	sha256: Mapped[] = mapped_column(nullable=False)
	fileSize: Mapped[] = mapped_column()
