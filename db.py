from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BaseModel = declarative_base()

db = create_engine("postgresql://postgres:1234@localhost/postgres")

Session = sessionmaker(autocommit=False, autoflush=False, bind=db)
session = Session()

