import sqlite3
import requests as r
import update_prices as TP
conn = sqlite3.connect("data.db")

#Clear item db
try:
    conn.execute("""--sql
    DROP TABLE item_prices
    """)
except:
    pass


#Copy default table
conn.execute("""--sql
CREATE TABLE item_prices AS SELECT * FROM item_prices_d WHERE 0
""")


#Insert IDS into db
request = r.get("https://api.guildwars2.com/v2/commerce/prices").json()

for entry in request:
    conn.execute("""--sql
    INSERT INTO item_prices (ID) 
    VALUES ({})
    """.format(entry))


#Get price data from api
TP.update_prices(conn)




#Execute and close db
conn.commit()
conn.close()