from sqlalchemy import insert
from DAOs import User


class UserService:
    def __init__(self, session) -> None:
        self.table = "user"
        self.session = session
        self.verbose = True
    
    def update(self):
        self.session.commit()

    def create(self, pseudo, email, pwd):
        u = User(pseudo=pseudo, email=email, pwd=pwd)
        self.session.add(u)
        self.session.commit()
        if self.verbose:
            print("user created")

    def delete(self, user)->bool:
        if user is not None:
            self.session.delete(user)
            self.session.commit()
            return True
        return False
    
    
    def find(self, id):
        return self.session.query(User).filter_by(id=id).first()
    
    
    def find_all(self):
        return list(self.session.query(User).all())


