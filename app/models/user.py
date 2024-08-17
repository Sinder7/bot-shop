from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    balance: Mapped[int] = mapped_column(nullable=False)
    bots: Mapped[lits["Bot"]] = relationship()
    created_at: Mapped[str] = mapped_column(nullable=False, default=datetime.utcnow)
    is_admin: Mapped[bool] = mapped_column(nullable=False, default=False)
    

class Bot(Base):
    __tablename__ = "bots"
    
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    created_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
class Transaction(Base):
    __tablename__ = "transactions"
    
    buyer_id: Mapped[int] = mapped_column(nullable=False, ForeignKey("users.id"))
    seller_id: Mapped[int] = mapped_column(nullable=False, ForeignKey("users.id"))
    
