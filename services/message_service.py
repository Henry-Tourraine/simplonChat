from DAOs import Message
from datetime import datetime

class MessageService:
    def __init__(self, session) -> None:
        self.session = session
        self.verbose = True
    
    def update(self):
        self.session.commit()

    def create(self, content, at, sender_id, receiver_id):
        u = Message(content=content, at=datetime.utcnow(), sender_id=sender_id, receiver_id=receiver_id)
        self.session.add(u)
        self.session.commit()
        if self.verbose:
            print("message created")

    def delete(self, message)->bool:
        if message is not None:
            self.session.delete(message)
            self.session.commit()
            return True
        return False
    
    
    def find(self, id):
        return self.session.query(Message).filter_by(id=id).first()
    
    def find_all(self):
        return list(self.session.query(Message).all())