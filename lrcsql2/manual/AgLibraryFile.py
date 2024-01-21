from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid

from datetime import datetime

class AgLibraryFile(Base):
    __tablename__ = "AgLibraryFile"
    id_local: Mapped[int] = mapped_column(Integer)
    id_global: Mapped[str] = mapped_column(Uuid)
    baseName: Mapped[str] = mapped_column(Text)
    errorMessage: Mapped[str] = mapped_column(Text, nullable=True)
    errorTime: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    extension: Mapped[str] = mapped_column(Text)
    externalModTime: Mapped[int] = mapped_column(Integer)
    folder: Mapped[int] = mapped_column(Integer)
    idx_filename: Mapped[str] = mapped_column(Text)
    importHash: Mapped[str] = mapped_column(Text)
    lc_idx_filename: Mapped[str] = mapped_column(Text)
    lc_idx_filenameExtension: Mapped[str] = mapped_column(Text)
    md5: Mapped[str] = mapped_column(Text, nullable=True)
    modTime: Mapped[int] = mapped_column(Integer)
    originalFilename: Mapped[str] = mapped_column(Text)
    sidecarExtensions: Mapped[str] = mapped_column(Text, nullable=True)