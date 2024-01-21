from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryKeyword(Base):
	__tablename__ = "AgLibraryKeyword"
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	dateCreated: Mapped[] = mapped_column(nullable=False)
	genealogy: Mapped[] = mapped_column(nullable=False)
	imageCountCache: Mapped[] = mapped_column()
	includeOnExport: Mapped[] = mapped_column(nullable=False)
	includeParents: Mapped[] = mapped_column(nullable=False)
	includeSynonyms: Mapped[] = mapped_column(nullable=False)
	keywordType: Mapped[] = mapped_column()
	lastApplied: Mapped[] = mapped_column()
	lc_name: Mapped[] = mapped_column()
	name: Mapped[] = mapped_column()
	parent: Mapped[] = mapped_column()
	id_local: Mapped[] = mapped_column(primary_key=True)
	tag1: Mapped[] = mapped_column(nullable=False)
	tag2: Mapped[] = mapped_column(nullable=False)
	value: Mapped[] = mapped_column(nullable=False)
	id_local: Mapped[] = mapped_column(primary_key=True)
	face: Mapped[] = mapped_column(nullable=False)
	keyFace: Mapped[] = mapped_column()
	rankOrder: Mapped[] = mapped_column()
	tag: Mapped[] = mapped_column(nullable=False)
	userPick: Mapped[] = mapped_column()
	userReject: Mapped[] = mapped_column()
	id_local: Mapped[] = mapped_column(primary_key=True)
	image: Mapped[] = mapped_column(nullable=False)
	tag: Mapped[] = mapped_column(nullable=False)
	id_local: Mapped[] = mapped_column(primary_key=True)
	occurrences: Mapped[] = mapped_column(nullable=False)
	popularity: Mapped[] = mapped_column(nullable=False)
	tag: Mapped[] = mapped_column(nullable=False, unique=True)
	id_local: Mapped[] = mapped_column(primary_key=True)
	keyword: Mapped[] = mapped_column(nullable=False)
	lc_name: Mapped[] = mapped_column()
	name: Mapped[] = mapped_column()
