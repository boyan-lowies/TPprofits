import sqlite3
conn = sqlite3.connect("data.db")

try:
    conn.execute("""--sql
    DROP TABLE item_prices_d;
    """)
except:
    pass

conn.execute("""--sql 
CREATE TABLE item_prices_d (
    id INT,
    name TEXT,
    buy_price INT,
    sell_price INT

)"""
)


conn.commit()
conn.close()