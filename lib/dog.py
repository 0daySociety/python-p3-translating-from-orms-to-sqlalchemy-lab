from models import Dog
from sqlalchemy import create_engine
from  sqlalchemy.orm import declarative_base,sessionmaker




def create_table(Base):
    if Base==declarative_base():
        engine=create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
    


def save(session, dog):
    dog=Dog()
    session=session()
    session.all([dog])
    session.commit()
  
   
    
   

def get_all(session):
    return session.query(Dog)

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name==name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id==id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(name==name,breed=breed)

def update_breed(session, dog, breed):
    return session.query(Dog).update({Dog.name:dog,Dog.breed:breed})