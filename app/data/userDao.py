from sqlalchemy.orm import Session

from app.data.modelo.usuario import Usuario



class UserDao:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list:
        return self.session.query(Usuario).all()

    def get_user_by_id(self, user_id : int)-> list:
        return self.session.query(Usuario).get(user_id)

    def add_user(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.query()
        self.session.commit()
        return usuario