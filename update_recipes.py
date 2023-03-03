import requests as rq
import sqlite3 
conn = sqlite3.connect("data.db")

request = rq.get("https://api.datawars2.ie/gw2/v2/recipes").json()
for entry in request:
    
    #convert request to processable list
    ingrediants = []
    for i,items in enumerate(entry['ingredients']):
       ingrediants.append([items["item_id"],items["count"]])
    for j in range(i,5):
        ingrediants.append([0,0])


    conn.execute("""--sql
    UPDATE 
        item_prices
    SET
        craft_1_id      = %i,
        craft_1_count   = %i,
        craft_2_id      = %i,
        craft_2_count   = %i,
        craft_3_id      = %i,
        craft_3_count   = %i,
        craft_4_id      = %i,
        craft_4_count   = %i,
        craft_5_id      = %i,
        craft_5_count   = %i
    WHERE
        id = %i
    """ % (
        ingrediants[0][0],
        ingrediants[0][1],
        ingrediants[1][0],
        ingrediants[1][1],
        ingrediants[2][0],
        ingrediants[2][1],
        ingrediants[3][0],
        ingrediants[3][1],
        ingrediants[4][0],
        ingrediants[4][1],
        entry['output_item_id']
    ))

conn.commit()
conn.close()

