from base import Base
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .connection import Connection
    from .call import Call
    from .message import Message
else:
    Connection = "Connection"
    Call = "Call"
    Message = "Message"

"""
User & Groups
id
pseudo
email
pwd
calls
connections
messages
"""
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    pseudo: Mapped[str] = mapped_column(String(30))
    email: Mapped[Optional[str]] = mapped_column(String(60))
    pwd = mapped_column(String())
    
    calls: Mapped[List["Call"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    connections: Mapped[List["Connection"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    received: Mapped[List["Message"]] = relationship(
        back_populates="receiver", cascade="all, delete-orphan"
    )

    sender: Mapped[List["Message"]] = relationship(
        back_populates="sender", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"