import pandas as pd
import xport
import xport.v56
from .database import db

def export():
    try:
        cursor = db.cursor()
        cursor.execute(f"select * from exchange")
    except Exception as e:
        print('Error: {}'.format(str(e)))

    try:
        df = pd.DataFrame(cursor.fetchall())
    except Exception as e:
        print('Error: {}'.format(str(e)))

    try:
        with open('example.xpt', 'wb') as f:
            xport.v56.dump(df, f)
    except Exception as e:
        print('Error: {}'.format(str(e)))
    db.close()
