from app import db, Card
import sqlite3
#create the database and the tables
db.create_all()

#seed data
'''u1 = User('R0b64170aa1a91a9D4eaafeffb03d9252', 0)
u2 = User('B1ccebf5213dbd0147653bf4111ee9081', 0)
u3 = User('F6751a566b78b1c87b18e73cae5549a8', 0)

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)'''

#commit changes
#db.session.commit()



'''with sqlite3.connect("cards.db") as conn:
	curr = conn.cursor()
	curr.execute("select * from cards")
	result = curr.fetchall()
	for r in result:
		row = Card(r[0],r[1],r[2],r[3],r[4])
		db.session.add(row)
		db.session.commit()


print "migration complete"'''
#db.session.commit()
	





		
		
		