import requests as r

def update_prices(conn):
    request = r.get("https://api.datawars2.ie/gw2/v1/items/json").json()
    for entry in request:
        conn.execute("""--sql
        UPDATE item_prices
        SET name = '%s', buy_price = %i, sell_price = %i
        WHERE id = %i
    """ % ( entry['name'].replace("\"","").replace("\'",""), 
            entry.get('buy_price',0), 
            entry.get('sell_price',0),
            entry['id'],))
