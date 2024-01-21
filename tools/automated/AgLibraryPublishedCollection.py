from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgLibraryPublishedCollection(Base):
	__tablename__ = "AgLibraryPublishedCollection"
	id_local: Mapped[] = mapped_column(primary_key=True)
	creationId: Mapped[] = mapped_column(nullable=False)
	genealogy: Mapped[] = mapped_column(nullable=False)
	imageCount: Mapped[] = mapped_column()
	isDefaultCollection: Mapped[] = mapped_column()
	name: Mapped[] = mapped_column(nullable=False)
	parent: Mapped[] = mapped_column()
	publishedUrl: Mapped[] = mapped_column()
	remoteCollectionId: Mapped[] = mapped_column()
	systemOnly: Mapped[] = mapped_column(nullable=False)
	id_local: Mapped[] = mapped_column(primary_key=True)
	collection: Mapped[] = mapped_column(nullable=False)
	content: Mapped[] = mapped_column()
	owningModule: Mapped[] = mapped_column()
	id_local: Mapped[] = mapped_column(primary_key=True)
	collection: Mapped[] = mapped_column(nullable=False)
	image: Mapped[] = mapped_column(nullable=False)
	pick: Mapped[] = mapped_column(nullable=False)
	positionInCollection: Mapped[] = mapped_column()
	id_local: Mapped[] = mapped_column(primary_key=True)
	id_global: Mapped[] = mapped_column(nullable=False, unique=True)
	collection: Mapped[] = mapped_column(nullable=False)
	label: Mapped[] = mapped_column()
	labelData: Mapped[] = mapped_column()
	labelGenerics: Mapped[] = mapped_column()
	labelType: Mapped[] = mapped_column(nullable=False)
