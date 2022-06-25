import os
from sqlalchemy import create_engine, insert, select
from sqlalchemy import Table, Column, Integer, String, ARRAY, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()
class Estate(Base):
    __tablename__ = "estates"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    urls = Column(ARRAY(String))

    def __init__(self, name, location, urls):
        self.name = name
        self.location = location
        self.urls = urls

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, location={self.location!r}, urls={self.urls!r})"


class DatabaseEstates:
    def __init__(self, user=os.environ["POSTGRES_USER"], passwd=os.environ["POSTGRES_PASS"],
                 host=os.environ["POSTGRES_HOST"], port=os.environ["POSTGRES_PORT"], db=os.environ["POSTGRES_DB"]):
        self.db_string = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"

        self.engine = create_engine(self.db_string)

        #Base.metadata.drop_all(self.engine)
        #print(self.engine.table_names())
        Base.metadata.create_all(self.engine)
        print(self.engine.table_names())

        self.Session = sessionmaker(bind=self.engine)

    def insert_all(self, data):
        session = self.Session()
        estates = [Estate(est['name'], est['location'], est['photo_urls']) for est in data]
        try:
            session.add_all(estates)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def process_item(self, item):
        session = self.Session()
        est = Estate(item['name'], item['location'], item['photo_urls'])

        try:
            session.add(est)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

    def view_all(self):
        session = self.Session()
        estates = session.query(Estate).all()

        for est in estates:
            print(est)
        session.close()

    def get_all(self):
        session = self.Session()
        data = session.query(Estate).all()
        session.close()
        return data
