from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryFaceCluster(Base):
	__tablename__ = "AgLibraryFaceCluster"
	id_local: Mapped[] = mapped_column(primary_key=True)
	keyFace: Mapped[] = mapped_column()
