from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgMetadataSearchIndex(Base):
	__tablename__ = "AgMetadataSearchIndex"
	id_local: Mapped[] = mapped_column(primary_key=True)
	exifSearchIndex: Mapped[] = mapped_column(nullable=False)
	image: Mapped[] = mapped_column()
	iptcSearchIndex: Mapped[] = mapped_column(nullable=False)
	otherSearchIndex: Mapped[] = mapped_column(nullable=False)
	searchIndex: Mapped[] = mapped_column(nullable=False)
