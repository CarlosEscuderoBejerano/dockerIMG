from sqlalchemy.orm import Session

from app.data.modelo.arma import Arma



class ArmaDao:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list:
        return self.session.query(Arma).all()

    def get_user_by_id(self, id : int)-> list:
        return self.session.query(Arma).get(id)