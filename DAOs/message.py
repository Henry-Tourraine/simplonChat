from base import Base
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from call import Call
from user import User
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User
else:
    User = "User"


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(30))
    at: Mapped[datetime] = mapped_column(DateTime)
    sender: Mapped[User] = relationship(back_populates="sent")
    receiver: Mapped[User] = relationship(back_populates="received")
    
    def __repr__(self) -> str:
        return f"Message(id={self.id!r}, at={self.at.strftime('%d/%m/%Y')!r}, sender={self.sender.id!r} receiver={self.receiver.id!r} )"