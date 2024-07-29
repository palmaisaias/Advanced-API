from sqlalchemy.orm import Mapped, mapped_column
from database import db, Base

class OrderItem(Base):
    __tablename__ = 'Order_Items'
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('Orders.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('Products.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(db.Integer, nullable=False)
    price: Mapped[float] = mapped_column(db.DECIMAL(10, 2), nullable=False)

    order: Mapped["Order"] = db.relationship('Order', back_populates='items')
    product: Mapped["Product"] = db.relationship('Product')
