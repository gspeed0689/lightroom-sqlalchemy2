from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryCollectionStackData(Base):
	__tablename__ = "AgLibraryCollectionStackData"
	stack: Mapped[] = mapped_column()
	collection: Mapped[] = mapped_column(nullable=False)
	stackCount: Mapped[] = mapped_column(nullable=False)
	stackParent: Mapped[] = mapped_column()
