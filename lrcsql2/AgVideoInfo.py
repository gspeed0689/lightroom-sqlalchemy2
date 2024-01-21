from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgVideoInfo(Base):
	__tablename__ = "AgVideoInfo"
	id_local: Mapped[] = mapped_column(primary_key=True)
	duration: Mapped[] = mapped_column()
	frame_rate: Mapped[] = mapped_column()
	has_audio: Mapped[] = mapped_column(nullable=False)
	has_video: Mapped[] = mapped_column(nullable=False)
	image: Mapped[] = mapped_column(nullable=False)
	poster_frame: Mapped[] = mapped_column(nullable=False)
	poster_frame_set_by_user: Mapped[] = mapped_column(nullable=False)
	trim_end: Mapped[] = mapped_column(nullable=False)
	trim_start: Mapped[] = mapped_column(nullable=False)
