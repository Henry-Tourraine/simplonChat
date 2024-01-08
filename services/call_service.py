from DAOs import Call
from datetime import datetime

class CallService:
    def __init__(self, session) -> None:
        self.session = session
        self.verbose = True

    def update(self):
        self.session.commit()

    def create(self, user_id):
        u = Call(end=None, start=datetime.now(), user_id=user_id)
        self.session.add(u)
        self.session.commit()
        if self.verbose:
            print("Call created")

    def delete(self, call)->bool:
        if call is not None:
            self.session.delete(call)
            self.session.commit()
            return True
        return False
    
    
    def find(self, id):
        return self.session.query(Call).filter_by(id=id).first()
    
    def find_all(self):
        return list(self.session.query(Call).all())