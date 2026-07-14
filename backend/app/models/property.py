from datetime import datetime

from sqlalchemy import ForeignKey, Integer, Numeric, String, Text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class Property(Base):
    __tablename__ = "properties"

    property_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    title: Mapped[str] = mapped_column(String(200), nullable=False)

    property_type: Mapped[str] = mapped_column(String(50), nullable=False)

    price: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)

    city: Mapped[str] = mapped_column(String(100), nullable=False)

    address: Mapped[str] = mapped_column(String(255), nullable=False)

    bedrooms: Mapped[int] = mapped_column(Integer)

    bathrooms: Mapped[int] = mapped_column(Integer)

    area_sqft: Mapped[int] = mapped_column(Integer)

    status: Mapped[str] = mapped_column(
        String(30),
        default="Available"
    )

    description: Mapped[str] = mapped_column(Text)

    created_by: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        default=datetime.utcnow
    )