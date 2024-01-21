from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgPhotoPropertySpec(Base):
	__tablename__ = "AgPhotoPropertySpec"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	flattenedAttributes: Mapped[] = mapped_column()
	key: Mapped[] = mapped_column(nullable=False)
	pluginVersion: Mapped[] = mapped_column(nullable=False)
	sourcePlugin: Mapped[] = mapped_column(nullable=False)
	userVisibleName: Mapped[] = mapped_column()
