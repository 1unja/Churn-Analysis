from scipy.io import arff
import pandas as pd
from sqlalchemy import create_engine

arff_file = arff.loadarff('/Users/lunja/Desktop/churn analysis/dataset')
df = pd.DataFrame(arff_file[0])
df = df.map(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)

# print(df.dtypes)

user = "root"
password = "Deker-On223"
host = "localhost"
database = "churn_db"

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{database}"
)

# df.to_sql(
#     name="customers",
#     con=engine,
#     if_exists="replace",
#     index=False
# )
