from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

from config import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

Base = declarative_base()

session = Session(engine)



