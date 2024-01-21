from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryUpdatedImages(Base):
	__tablename__ = "AgLibraryUpdatedImages"
	image: Mapped[] = mapped_column(primary_key=True)
