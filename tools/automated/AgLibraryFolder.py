from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryFolder(Base):
	__tablename__ = "AgLibraryFolder"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	parentId: Mapped[] = mapped_column()
	pathFromRoot: Mapped[] = mapped_column(nullable=False)
	rootFolder: Mapped[] = mapped_column(nullable=False)
	visibility: Mapped[] = mapped_column()
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	favorite: Mapped[] = mapped_column()
	folder: Mapped[] = mapped_column(nullable=False)
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	folder: Mapped[] = mapped_column(nullable=False)
	label: Mapped[] = mapped_column()
	labelData: Mapped[] = mapped_column()
	labelGenerics: Mapped[] = mapped_column()
	labelType: Mapped[] = mapped_column(nullable=False)
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
