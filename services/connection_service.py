from DAOs import Connection
from datetime import datetime

class ConnectionService:
    def __init__(self, session) -> None:
        self.session = session
        self.verbose = True

    def update(self):
        self.session.commit()

    def create(self, user_id):
        u = Connection(end=None, start=datetime.now(), user_id=user_id)
        self.session.add(u)
        self.session.commit()
        if self.verbose:
            print("Connection created")

    def delete(self, connection)->bool:
        if connection is not None:
            self.session.delete(connection)
            self.session.commit()
            return True
        return False
    
    
    def find(self, id):
        return self.session.query(Connection).filter_by(id=id).first()
    
    def find_all(self):
        return list(self.session.query(Connection).all())