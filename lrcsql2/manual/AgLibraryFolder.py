from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid

from datetime import datetime

class AgLibraryFolder(Base):
    __tablename__ = "AgLibraryFolder"
    id_local: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_global: Mapped[str] = mapped_column(Uuid)
    parentId: Mapped[int] = mapped_column(Integer, nullable=True)
    pathFromRoot: Mapped[str] = mapped_column(Text)
    rootFolder: Mapped[int] = mapped_column(Integer)
    visibility: Mapped[int] = mapped_column(Integer, nullable=True)