from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from database import db, Base

class Cart(Base):
    __tablename__ = 'Carts'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('Customers.id'), nullable=False)

    items: Mapped[List["CartItem"]] = db.relationship('CartItem', back_populates='cart')
