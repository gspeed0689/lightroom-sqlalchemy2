from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryOzCommentIds(Base):
	__tablename__ = "AgLibraryOzCommentIds"
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	ozSpaceId: Mapped[] = mapped_column(nullable=False)
	ozAssetId: Mapped[] = mapped_column(nullable=False)
	ozCommentId: Mapped[] = mapped_column(nullable=False)
	timestamp: Mapped[] = mapped_column(nullable=False)
