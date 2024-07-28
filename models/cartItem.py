from sqlalchemy.orm import Mapped, mapped_column
from database import db, Base

class CartItem(Base):
    __tablename__ = 'Cart_Items'
    id: Mapped[int] = mapped_column(primary_key=True)
    cart_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('Carts.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('Products.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(db.Integer, nullable=False)
    price: Mapped[float] = mapped_column(db.DECIMAL(10, 2), nullable=False)

    cart: Mapped["Cart"] = db.relationship('Cart', back_populates='items')
    product: Mapped["Product"] = db.relationship('Product')