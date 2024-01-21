from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgDevelopAdditionalMetadata(Base):
	__tablename__ = "AgDevelopAdditionalMetadata"
	id_local: Mapped[] = mapped_column(primary_key=True)
	hasDepthMap: Mapped[] = mapped_column()
	hasEnhance: Mapped[] = mapped_column()
	image: Mapped[] = mapped_column()
