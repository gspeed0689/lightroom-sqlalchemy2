from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgSpecialSourceContent(Base):
	__tablename__ = "AgSpecialSourceContent"
	id_local: Mapped[] = mapped_column(primary_key=True)
	content: Mapped[] = mapped_column()
	owningModule: Mapped[] = mapped_column()
	source: Mapped[] = mapped_column(nullable=False)
