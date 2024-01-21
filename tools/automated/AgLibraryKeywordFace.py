from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryKeywordFace(Base):
	__tablename__ = "AgLibraryKeywordFace"
	id_local: Mapped[] = mapped_column(primary_key=True)
	face: Mapped[] = mapped_column(nullable=False)
	keyFace: Mapped[] = mapped_column()
	rankOrder: Mapped[] = mapped_column()
	tag: Mapped[] = mapped_column(nullable=False)
	userPick: Mapped[] = mapped_column()
	userReject: Mapped[] = mapped_column()
