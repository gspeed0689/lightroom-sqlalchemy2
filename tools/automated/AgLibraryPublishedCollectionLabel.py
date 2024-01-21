from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryPublishedCollectionLabel(Base):
	__tablename__ = "AgLibraryPublishedCollectionLabel"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	collection: Mapped[] = mapped_column(nullable=False)
	label: Mapped[] = mapped_column()
	labelData: Mapped[] = mapped_column()
	labelGenerics: Mapped[] = mapped_column()
	labelType: Mapped[] = mapped_column(nullable=False)
