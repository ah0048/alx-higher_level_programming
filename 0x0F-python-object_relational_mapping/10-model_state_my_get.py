#!/usr/bin/python3
'''query State class'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    database = argv[3]
    state_name = argv[4]

    conn_string = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        user, passwd, database)
    engine = create_engine(conn_string, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    req_state = session.query(State).order_by(State.id).filter(
        State.name == state_name).first()
    if req_state:
        print("{}".format(req_state.id))
    else:
        print("Not found")
    session.close()
