from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryFile(Base):
	__tablename__ = "AgLibraryFile"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	baseName: Mapped[] = mapped_column(nullable=False)
	errorMessage: Mapped[] = mapped_column()
	errorTime: Mapped[] = mapped_column()
	extension: Mapped[] = mapped_column(nullable=False)
	externalModTime: Mapped[] = mapped_column()
	folder: Mapped[] = mapped_column(nullable=False)
	idx_filename: Mapped[] = mapped_column(nullable=False)
	importHash: Mapped[] = mapped_column()
	lc_idx_filename: Mapped[] = mapped_column(nullable=False)
	lc_idx_filenameExtension: Mapped[] = mapped_column(nullable=False)
	md5: Mapped[] = mapped_column()
	modTime: Mapped[] = mapped_column()
	originalFilename: Mapped[] = mapped_column(nullable=False)
	sidecarExtensions: Mapped[] = mapped_column()
	fileId: Mapped[] = mapped_column(primary_key=True)
	sha256: Mapped[] = mapped_column(nullable=False)
	fileSize: Mapped[] = mapped_column()
