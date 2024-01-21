from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgPhotoComment(Base):
	__tablename__ = "AgPhotoComment"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	comment: Mapped[] = mapped_column()
	commentRealname: Mapped[] = mapped_column()
	commentUsername: Mapped[] = mapped_column()
	dateCreated: Mapped[] = mapped_column()
	photo: Mapped[] = mapped_column(nullable=False)
	remoteId: Mapped[] = mapped_column(nullable=False)
	remotePhoto: Mapped[] = mapped_column()
	url: Mapped[] = mapped_column()
