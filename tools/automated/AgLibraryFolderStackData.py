from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryFolderStackData(Base):
	__tablename__ = "AgLibraryFolderStackData"
	stack: Mapped[] = mapped_column()
	stackCount: Mapped[] = mapped_column(nullable=False)
	stackParent: Mapped[] = mapped_column()
