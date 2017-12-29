from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlou')
Base = declarative_base()


class Repository(Base):
	__tablename__ = 'repositories'

	id = Column(Integer, primary_key=True)
	name = Column(String(64), index=True)
	update_time = Column(DateTime)
	commit = Column(Integer)
	branches = Column(Integer)
	releases = Column(Integer)

if __name__ == '__main__':
	Base.metadata.create_all(engine)
