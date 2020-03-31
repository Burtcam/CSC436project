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
    #one to many
    termschild = relationship("mastervendor")
    termschild2 = relationship("orderheader")



class mastervendor(Base):
    __tablename__='mastervendor'

    vendorId = sqlalchemy.Column(sqlalchemy.String(length=48, primary_key=True))
    contactName= sqlalchemy.Column(sqlalchemy.String(length=50))
    vendorName = sqlalchemy.Column(sqlalchemy.String(length=48))
    country = sqlalchemy.Column(sqlalchemy.String(length=48))
    state = sqlalchemy.Column(sqlalchemy.String(length=48))
    zip = sqlalchemy.Column(sqlalchemy.Integer)
    address = sqlalchemy.Column(sqlalchemy.String(length=50))
    termsID = sqlalchemy.Column(sqlalchemy.String(length=12), ForeignKey('termscodes.termsID'))
    #one to many with masteritem
    childvendor = relationship("masteritem")
    childvendor2 = relationship("orderheader")


class masteritem(Base):
    __tablename__ = 'masteritem'

    itemID = sqlalchemy.Column(sqlalchemy.String(length=48,primary_key=True))
    lastPriceChange = sqlalchemy.Column(sqlalchemy.Date)
    previousCost = sqlalchemy.Column(sqlalchemy.Float)
    vendorId = sqlalchemy.Column(sqlalchemy.String(length=48),ForeignKey('mastervendor.vendorId'))
    cost = sqlalchemy.Column(sqlalchemy.Float)
    intialPurchaseDate = sqlalchemy.Column(sqlalchemy.Date)

    #connection to inventory
    childitem = relationship("inventory")
    childitem2 = relationship("lineitem")


class inventory(Base):
    __tablename__ = 'inventory'

    recordnum = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    itemID = sqlalchemy.Column(sqlalchemy.String(length=48), ForeignKey('masteritem.itemID'))
    onhand = sqlalchemy.Column(sqlalchemy.Integer)
    location = sqlalchemy.Column(sqlalchemy.String(length=12))

class orderheader(Base):
    __tablename__ = 'orderheader'

    orderreceived = sqlalchemy.Column(sqlalchemy.Date)
    vendorId = itemID = sqlalchemy.Column(sqlalchemy.String(length=48), ForeignKey('vendormaster.vendorId'))
    orderdate = sqlalchemy.Column(sqlalchemy.Date)
    orderID = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    shipdate = sqlalchemy.Column(sqlalchemy.Date)
    Cost = sqlalchemy.Column(sqlalchemy.Float)
    termsID = sqlalchemy.Column(sqlalchemy.String(length=12),ForeignKey('termscodes.termsID'))
    childorder = relationship("lineitem")

#foreign on orderid and itemid todo
class lineitem(Base):
    __tablename__ = 'lineitem'

    itemID = sqlalchemy.Column(sqlalchemy.String(length=48), ForeignKey('masteritem.itemID'))
    quantity = sqlalchemy.Column(sqlalchemy.Integer)
    lineID = sqlalchemy.Column(sqlalchemy.Integer)
    orderID = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('orderheader.orderID'))
    Cost = sqlalchemy.Column(sqlalchemy.Float, ForeignKey('masteritem.cost'))


    def __repr__(self):
        return "<User(name='{0}', fullname='{1}', nickname='{2}')>".format(
            self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# Add a user
jwk_user = User(name='Cam', fullname='Cam Burt', nickname='&#x1f42c;')
session.add(jwk_user)
session.commit()

# Query the user
our_user = session.query(User).filter_by(name='jesper').first()
print('\nOur User:')
print(our_user)
print('Nick name in hex: {0}'.format(our_user.nickname.encode('utf-8')))