from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, CategoryItem

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to metadata of the Base class
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Food Category
food = Category(name="Food", user_id=1)
session.add(food)
session.commit()

item1 = CategoryItem(user_id=1, name="Milk", description="One Gallon, non-organic", price="$2.00", category=food)
session.add(item1)
session.commit()

item2 = CategoryItem(user_id=1, name="Egg", description="One dozen, non-organic", price="$.99", category=food)
session.add(item2)
session.commit()

item3 = CategoryItem(user_id=1, name="Cereal", description="One Box. Preferred brand: Post honey bounches of oats", price="$2.00", category=food)
session.add(item3)
session.commit()

item4 = CategoryItem(user_id=1, name="Cake Mix", description="One Box", price="$0.50", category=food)
session.add(item3)
session.commit()

# Personal Care Category
personalCare = Category(user_id=1, name="Personal Care")
session.add(personalCare)
session.commit()

item1 = CategoryItem(user_id=1, name="Body Wash", description="16 oz bottle", price="$2.00", category=personalCare)
session.add(item1)
session.commit()

item2 = CategoryItem(user_id=1, name="Shampoo", description="16 oz bottle. Head & Shoulder is more expensive, best deal is $2 per bottle.", price="$1.00", category=personalCare)
session.add(item2)
session.commit()

item3 = CategoryItem(user_id=1, name="Conditioner", description="16 oz bottle", price="$1.00", category=personalCare)
session.add(item3)
session.commit()

item4 = CategoryItem(user_id=1, name="Mouth Wash", description="16 oz bottle", price="$1.00", category=personalCare)
session.add(item4)
session.commit()

# Household Category
household = Category(user_id=1, name="Household")
session.add(household)
session.commit()

item1 = CategoryItem(user_id=1, name="Laundry Detergent", description="50 oz bottle. Preferred brands: Persil, Tide. Tide red bottles costs more, Tide simply clean can be found at $1", price="$1.00", category=household)
session.add(item1)
session.commit()

item2 = CategoryItem(user_id=1, name="Paper Towel", description="One regular roll. Preferred brands: Bounty, Brawny", price="$0.50", category=household)
session.add(item2)
session.commit()

item3 = CategoryItem(user_id=1, name="Toilet Paper", description="One regular roll. Preferred brands: Charmin, Quilted Northern, Cottonelle", price="$0.15", category=household)
session.add(item3)
session.commit()

item4 = CategoryItem(user_id=1, name="Trash bag", description="13 gallon kitchen tall. Best deal found at Costco", price="$0.06", category=household)
session.add(item4)
session.commit()

# Pharmacy Category
pharmacy = Category(user_id=1, name="Pharmacy")
session.add(pharmacy)
session.commit()

item1 = CategoryItem(user_id=1, name="Centrum", description="65 pc bottle", price="$1.00", category=pharmacy)
session.add(item1)
session.commit()

item2 = CategoryItem(user_id=1, name="Pain Killer", description="20 pc bottle", price="$1.00", category=pharmacy)
session.add(item2)
session.commit()

item3 = CategoryItem(user_id=1, name="Cough drops", description="50 pc bag", price="$1.00", category=pharmacy)
session.add(item3)
session.commit()

print "Added category items!"
