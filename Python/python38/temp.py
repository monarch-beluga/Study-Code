
import pandas as pd
from sqlalchemy import create_engine

# conn = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/shop', encoding='utf8')
conn = create_engine('mysql+pymysql://root:123456@192.168.28.183:3306/meteodata', encoding='utf8')
f = r'E:\public\Data\station.txt'

df = pd.read_csv(f, header=0)
df1 = df.rename(columns={'台站':'code', 'evela':'elev'})
df1.to_sql('station', conn, if_exists='append', index=False, index_label=False)
