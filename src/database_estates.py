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
<<<<<<< HEAD
    def __init__(self, user=os.environ["POSTGRES_USER"], passwd=os.environ["POSTGRES_PASS"],
                 host=os.environ["POSTGRES_HOST"], port=os.environ["POSTGRES_PORT"], db=os.environ["POSTGRES_DB"]):
=======
    def __init__(self, user='postgres', passwd='burgermenu',
                 host='localhost', port='5432', db='postgres'):
>>>>>>> 3d2574ce6e7633afa6786c76fe01d70a3f2226ff
        self.db_string = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"

        self.engine = create_engine(self.db_string)

        #Base.metadata.drop_all(self.engine)
        #print(self.engine.table_names())
        Base.metadata.create_all(self.engine)
        print(self.engine.table_names())

        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()

    def insert(self, data):
        estates = [Estate(est['name'], est['location'], est['photo_urls']) for est in data]
        self.session.add_all(estates)
        self.session.commit()

    def view_all(self):
        estates = self.session.query(Estate).all()

        for est in estates:
            print(est)

    def get_all(self):
        return self.session.query(Estate).all()

    def __del__(self):
        self.session.close()
