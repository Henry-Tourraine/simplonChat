from DAOs import Invitation
from datetime import datetime

class InvitationService:
    def __init__(self, session) -> None:
        self.session = session
        self.verbose = True

    def update(self):
        self.session.commit()

    def create(self, content, at, sender_id, receiver_id):
        u = Invitation(accepted=None, at=datetime.now(), sender_id=sender_id, receiver_id=receiver_id)
        self.session.add(u)
        self.session.commit()
        if self.verbose:
            print("Invitation created")
    
    def delete(self, invitation)->bool:
        if invitation is not None:
            self.session.delete(invitation)
            self.session.commit()
            return True
        return False
    
    
    def find(self, id):
        return self.session.query(Invitation).filter_by(id=id).first()
    
    def find_all(self):
        return list(self.session.query(Invitation).all())