from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryFolderFavorite(Base):
	__tablename__ = "AgLibraryFolderFavorite"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	favorite: Mapped[] = mapped_column()
	folder: Mapped[] = mapped_column(nullable=False)
