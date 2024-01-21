from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgRemotePhoto(Base):
	__tablename__ = "AgRemotePhoto"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	collection: Mapped[] = mapped_column(nullable=False)
	commentCount: Mapped[] = mapped_column()
	developSettingsDigest: Mapped[] = mapped_column()
	fileContentsHash: Mapped[] = mapped_column()
	fileModTimestamp: Mapped[] = mapped_column()
	metadataDigest: Mapped[] = mapped_column()
	mostRecentCommentTime: Mapped[] = mapped_column()
	orientation: Mapped[] = mapped_column()
	photo: Mapped[] = mapped_column(nullable=False)
	photoNeedsUpdating: Mapped[] = mapped_column()
	publishCount: Mapped[] = mapped_column()
	remoteId: Mapped[] = mapped_column()
	serviceAggregateRating: Mapped[] = mapped_column()
	url: Mapped[] = mapped_column()
