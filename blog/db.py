from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# Define the MySQL engine using MySQL Connector/Python
engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://root:CSC436!@localhost:3306/gameshop',
    echo=True)

# Define and create the table
Base = declarative_base()


class termscodes(Base):
    __tablename__='termscodes'
    termsID = sqlalchemy.Column(sqlalchemy.String(length=12),primary_key=True)
    discount = sqlalchemy.Column(sqlalchemy.Decimal)
    allowance = sqlalchemy.Column(sqlalchemy.Decimal)
    daysToEarnDiscount= sqlalchemy.Column(sqlalchemy.Integer)



#todo add foreign key to terms id
class mastervendor(Base):
    __tablename__='mastervendor'

    vendorId = sqlalchemy.Column(sqlalchemy.String(length=48, primary_key=True))
    contactName= sqlalchemy.Column(sqlalchemy.String(length=50))
    vendorName = sqlalchemy.Column(sqlalchemy.String(length=48))
    country = sqlalchemy.Column(sqlalchemy.String(length=48))
    state = sqlalchemy.Column(sqlalchemy.String(length=48))
    zip = sqlalchemy.Column(sqlalchemy.Integer)
    address = sqlalchemy.Column(sqlalchemy.String(length=50))
    termsID = sqlalchemy.Column(sqlalchemy.String(length=12))



#masteritemtable todo add foreign key on vendorId to vendormaster
class masteritem(Base):
    __tablename__ = 'masteritem'

    itemID = sqlalchemy.Column(sqlalchemy.String(length=48,primary_key=True))
    lastPriceChange = sqlalchemy.Column(sqlalchemy.Date)
    previousCost = sqlalchemy.Column(sqlalchemy.Float)
    vendorId = sqlalchemy.Column(sqlalchemy.String(length=48))
    cost = sqlalchemy.Column(sqlalchemy.Float)
    intialPurchaseDate = sqlalchemy.Column(sqlalchemy.Date)


#inventorytable todo add foreign key on itemId to masteritem
class inventory(Base):
    __tablename__ = 'inventory'

    recordnum = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    itemID = sqlalchemy.Column(sqlalchemy.String(length=48), foreign_key=True)
    onhand = sqlalchemy.Column(sqlalchemy.Integer)
    location = sqlalchemy.Column(sqlalchemy.String(length=12))

#TODO add foreign key on terms id, vendorID
class orderheader(Base):
    __tablename__ = 'orderheader'

    orderreceived = sqlalchemy.Column(sqlalchemy.Date)
    vendorId = itemID = sqlalchemy.Column(sqlalchemy.String(length=48))
    orderdate = sqlalchemy.Column(sqlalchemy.Date)
    orderID = sqlalchemy.Column(sqlalchemy.Integer)
    shipdate = sqlalchemy.Column(sqlalchemy.Date)
    cost = sqlalchemy.Column(sqlalchemy.Float)
    termsID = termsID = sqlalchemy.Column(sqlalchemy.String(length=12))

class lineitem(Base):
    __tablename__ = 'lineitem'

    itemID = sqlalchemy.Column(sqlalchemy.String(length=48), foreign_key=True)
    quantity = sqlalchemy.Column(sqlalchemy.Integer)
    lineID = 

    def __repr__(self):
        return "<User(name='{0}', fullname='{1}', nickname='{2}')>".format(
            self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# Add a user
jwk_user = User(name='jesper', fullname='Jesper Wisborg Krogh', nickname='&#x1f42c;')
session.add(jwk_user)
session.commit()

# Query the user
our_user = session.query(User).filter_by(name='jesper').first()
print('\nOur User:')
print(our_user)
print('Nick name in hex: {0}'.format(our_user.nickname.encode('utf-8')))