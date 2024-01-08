from base import Base
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User
else:
    User = "User"



class Invitation(Base):
    __tablename__ = "invitations"

    id: Mapped[int] = mapped_column(primary_key=True)
    at: Mapped[datetime] = mapped_column(DateTime)
    sender: Mapped[User] = relationship()
    receiver: Mapped[User] = relationship()
    accepted: Mapped[Optional[datetime]] = mapped_column(DateTime)

    def __repr__(self) -> str:
        return f"Invitation(at={self.at.strftime('%d/%m/%Y')}, accepted={self.accepted is not None}, sender={self.sender.id!r} receiver={self.receiver.id!r})"