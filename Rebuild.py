import sqlite3
import requests as r
import update_prices as TP
import update_recipes as R
conn = sqlite3.connect("data.db")


#Clear item db
try:
    conn.execute("""--sql
    DROP TABLE item_prices
    """)
except:
    pass
print("Item db cleared")


#Copy default table
conn.execute("""--sql
CREATE TABLE item_prices AS SELECT * FROM item_prices_d WHERE 0
""")
print("Coppied default table")

#Insert tradable IDS into db
request = r.get("https://api.guildwars2.com/v2/commerce/prices").json()
for entry in request:
    conn.execute("""--sql
    INSERT INTO item_prices (ID) 
    VALUES ({})
    """.format(entry))
print("Inserted IDs")

#Get price data from api
TP.update_prices(conn)
print("Updated prices")


#Get recipe data
R.update_recipes(conn)
print("Updated recipes")


#Execute and close db
conn.commit()
conn.close()
print("Done")