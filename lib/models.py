#!/usr/bin/env python3
from sqlalchemy import (Column, String, Integer,create_engine)
from sqlalchemy.orm import declarative_base,sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

    def __repr__(self):
        return f"animal {self.id}: " \
            + f" name {self.name}, " \
            + f"breed  {self.breed}"
        



if __name__=="__main__":
    try:
        engine=create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session=sessionmaker(bind=engine)
        session=session()
        

        rough=Dog(name="rough",breed="German Shepard")
        softie=Dog(name="sofie",breed="rotwailer")
        session.add_all([rough,softie])
        session.commit()

        for animal in session.query(Dog):
            print(animal)



    except Exception as e:
        print("got this error ", str(e))    



 
