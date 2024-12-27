import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# DB Connector
engine = sqlalchemy.create_engine('sqlite:///enterprise.db', echo=True)

# Maping
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
        return "<User(name={}, last_name={}, age={})>".format(self.name, self.last_name, self.age)
    
# Creating the table in DB
Base.metadata.create_all(engine)

# Creating user
user = User(name='Enzo',last_name='Francisco', age=20)

# Creating session
Session = sessionmaker(bind=engine)

session = Session()

# Adding objects (INSERT)
session.add(user)
session.add_all({
    User(name='gabriel',last_name='Santos', age=27),
    User(name='pedro',last_name='Francisco', age=22),
})
session.commit()
session.new