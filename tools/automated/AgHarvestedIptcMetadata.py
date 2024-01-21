from base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, Integer, Float, DateTime, Date, Time, Boolean, Uuid
from sqlalchemy import BLOB

from datetime import datetime

class AgHarvestedIptcMetadata(Base):
	__tablename__ = "AgHarvestedIptcMetadata"
	id_local: Mapped[] = mapped_column(primary_key=True)
	image: Mapped[] = mapped_column()
	cityRef: Mapped[] = mapped_column()
	copyrightState: Mapped[] = mapped_column()
	countryRef: Mapped[] = mapped_column()
	creatorRef: Mapped[] = mapped_column()
	isoCountryCodeRef: Mapped[] = mapped_column()
	jobIdentifierRef: Mapped[] = mapped_column()
	locationDataOrigination: Mapped[] = mapped_column(nullable=False)
	locationGPSSequence: Mapped[] = mapped_column(nullable=False)
	locationRef: Mapped[] = mapped_column()
	stateRef: Mapped[] = mapped_column()
