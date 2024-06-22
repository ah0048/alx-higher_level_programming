#!/usr/bin/python3
'''query State class'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    conn_string = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        user, passwd, database)
    engine = create_engine(conn_string, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State, City).order_by(City.id).filter(
        City.state_id == State.id).all()
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
