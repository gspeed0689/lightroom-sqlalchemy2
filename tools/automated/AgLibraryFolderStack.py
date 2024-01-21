from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryFolderStack(Base):
	__tablename__ = "AgLibraryFolderStack"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	collapsed: Mapped[] = mapped_column(nullable=False)
	text: Mapped[] = mapped_column(nullable=False)
	stack: Mapped[] = mapped_column()
	stackCount: Mapped[] = mapped_column(nullable=False)
	stackParent: Mapped[] = mapped_column()
	id_local: Mapped[] = mapped_column(primary_key=True)
	collapsed: Mapped[] = mapped_column(nullable=False)
	image: Mapped[] = mapped_column(nullable=False)
	position: Mapped[] = mapped_column(nullable=False)
	stack: Mapped[] = mapped_column(nullable=False)
