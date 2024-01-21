from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgFolderContent(Base):
	__tablename__ = "AgFolderContent"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	containingFolder: Mapped[] = mapped_column(nullable=False)
	content: Mapped[] = mapped_column()
	name: Mapped[] = mapped_column()
	owningModule: Mapped[] = mapped_column()
