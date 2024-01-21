from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryOzFeedbackInfo(Base):
	__tablename__ = "AgLibraryOzFeedbackInfo"
	id_local: Mapped[] = mapped_column(primary_key=True)
	image: Mapped[] = mapped_column(nullable=False)
	lastFeedbackTime: Mapped[] = mapped_column()
	lastReadTime: Mapped[] = mapped_column()
	newCommentCount: Mapped[] = mapped_column(nullable=False)
	newFavoriteCount: Mapped[] = mapped_column(nullable=False)
	ozAssetId: Mapped[] = mapped_column(nullable=False)
	ozCatalogId: Mapped[] = mapped_column(nullable=False)
	ozSpaceId: Mapped[] = mapped_column(nullable=False)
