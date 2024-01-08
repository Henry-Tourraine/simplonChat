import sqlalchemy as db
from .base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .user import User
from .call import Call
from .connection import Connection
from .invitation import Invitation
from .message import Message


class Context:
    def __init__(self):
        engine = create_engine(
            "postgresql+psycopg2://postgres:root@localhost:5432/simplonchat?client_encoding=utf8",
            
            isolation_level = "REPEATABLE READ",
            echo=True
        )
        Call
        User
        Message
        Invitation
        Connection
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        self.session = Session()

    def getSession(self):
        return self.session

if __name__ == "__main__":
    Context()