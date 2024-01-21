from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid

from datetime import datetime

class Adobe_images(Base):
    __tablename__ = "Adobe_images"
    id_local: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_global: Mapped[str] = mapped_column(Uuid)
    aspectRatioCache: Mapped[float] = mapped_column(Float)
    bitDepth: Mapped[int] = mapped_column(Integer)
    captureTime: Mapped[datetime] = mapped_column(DateTime)
    colorChannels: Mapped[int] = mapped_column(Integer)
    colorLabels: Mapped[str] = mapped_column(Text, nullable=True)
    colorMode: Mapped[int] = mapped_column(Integer)
    copyCreationTime: Mapped[int] = mapped_column(Integer, nullable=True)
    copyName: Mapped[str] = mapped_column(Text, nullable=True)
    copyReason: Mapped[str] = mapped_column(Text, nullable=True) #unknown
    developSettingsIDCache: Mapped[int] = mapped_column(Integer)
    editLock: Mapped[int] = mapped_column(Integer)
    fileFormat: Mapped[str] = mapped_column(Text)
    fileHeight: Mapped[int] = mapped_column(Integer)
    fileWidth: Mapped[int] = mapped_column(Integer)
    hasMissingSidecars: Mapped[int] = mapped_column(Integer, nullable=True)
    masterImage: Mapped[int] = mapped_column(Integer, nullable=True)
    orientation: Mapped[str] = mapped_column(Text)
    originalCaptureTime: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    originalRootEntity: Mapped[int] = mapped_column(Integer, nullable=True)
    panningDistanceH: Mapped[int] = mapped_column(Integer, nullable=True) #unknown
    panningDistanceV: Mapped[int] = mapped_column(Integer, nullable=True) #unknown
    pick: Mapped[int] = mapped_column(Integer)
    positionInFolder: Mapped[str] = mapped_column(Text)
    propertiesCache: Mapped[int] = mapped_column(Integer)
    pyramidIDCache: Mapped[str] = mapped_column(Text)
    rating: Mapped[int] = mapped_column(Integer, nullable=True)
    rootFile: Mapped[int] = mapped_column(Integer)
    sidecarStatus: Mapped[int] = mapped_column(Integer)
    touchCount: Mapped[int] = mapped_column(Integer)
    touchTime: Mapped[float] = mapped_column(Float)