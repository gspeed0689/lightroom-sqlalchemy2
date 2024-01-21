from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryFace(Base):
	__tablename__ = "AgLibraryFace"
	id_local: Mapped[] = mapped_column(primary_key=True)
	bl_x: Mapped[] = mapped_column()
	bl_y: Mapped[] = mapped_column()
	br_x: Mapped[] = mapped_column()
	br_y: Mapped[] = mapped_column()
	cluster: Mapped[] = mapped_column()
	compatibleVersion: Mapped[] = mapped_column()
	ignored: Mapped[] = mapped_column()
	image: Mapped[] = mapped_column(nullable=False)
	imageOrientation: Mapped[] = mapped_column(nullable=False)
	orientation: Mapped[] = mapped_column()
	origination: Mapped[] = mapped_column(nullable=False)
	propertiesCache: Mapped[] = mapped_column()
	regionType: Mapped[] = mapped_column(nullable=False)
	skipSuggestion: Mapped[] = mapped_column()
	tl_x: Mapped[] = mapped_column(nullable=False)
	tl_y: Mapped[] = mapped_column(nullable=False)
	touchCount: Mapped[] = mapped_column(nullable=False)
	touchTime: Mapped[] = mapped_column(nullable=False)
	tr_x: Mapped[] = mapped_column()
	tr_y: Mapped[] = mapped_column()
	version: Mapped[] = mapped_column()
	id_local: Mapped[] = mapped_column(primary_key=True)
	keyFace: Mapped[] = mapped_column()
	id_local: Mapped[] = mapped_column(primary_key=True)
	data: Mapped[] = mapped_column()
	face: Mapped[] = mapped_column(nullable=False)
