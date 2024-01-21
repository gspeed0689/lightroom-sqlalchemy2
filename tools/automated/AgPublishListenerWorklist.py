from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgPublishListenerWorklist(Base):
	__tablename__ = "AgPublishListenerWorklist"
	id_local: Mapped[] = mapped_column(primary_key=True)
	taskID: Mapped[] = mapped_column(nullable=False, unique=True)
	taskStatus: Mapped[] = mapped_column(nullable=False)
	whenPosted: Mapped[] = mapped_column(nullable=False)
