from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgOutputImageAsset(Base):
	__tablename__ = "AgOutputImageAsset"
	id_local: Mapped[] = mapped_column(primary_key=True)
	assetId: Mapped[] = mapped_column(nullable=False)
	collection: Mapped[] = mapped_column(nullable=False)
	image: Mapped[] = mapped_column(nullable=False)
	moduleId: Mapped[] = mapped_column(nullable=False)
