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
    sell_price INT,
    craft_count INT,
    craft_1_id INT,
    craft_1_count INT,
    craft_2_id INT,
    craft_2_count INT,
    craft_3_id INT,
    craft_3_count INT,
    craft_4_id INT,
    craft_4_count INT,
    craft_5_id INT,
    craft_5_count INT


)"""
)


conn.commit()
conn.close()