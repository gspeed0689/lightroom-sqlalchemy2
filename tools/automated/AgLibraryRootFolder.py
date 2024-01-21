from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryRootFolder(Base):
	__tablename__ = "AgLibraryRootFolder"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	absolutePath: Mapped[] = mapped_column(nullable=False, unique=True)
	name: Mapped[] = mapped_column(nullable=False)
	relativePathFromCatalog: Mapped[] = mapped_column()
