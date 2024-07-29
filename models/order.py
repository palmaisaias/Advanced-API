from typing import List
import datetime
from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from models.orderItem import OrderItem

class Order(Base):
    __tablename__ = 'Orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[datetime.date] = mapped_column(db.Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('Customers.id'))

    customer: Mapped["Customer"] = db.relationship("Customer", back_populates="orders")
    items: Mapped[List["OrderItem"]] = db.relationship("OrderItem", back_populates="order")

