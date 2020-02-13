import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('C:/proyecto/bdd-servicios-2012empalme.csv', header = 0, encoding='latin-1')
print(df)

engine = create_engine('mysql://root:a-ha14091982@localhost/test2')
with engine.connect() as conn, conn.begin():
    df.to_sql('csv', conn, if_exists='append', index=False)
