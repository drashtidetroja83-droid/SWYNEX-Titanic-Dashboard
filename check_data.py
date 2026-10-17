# import pandas as pd
# df = pd.read_excel("SWYNEX_Titanic_Data_Cleaned.xlsx")
# print(df.head(10))

import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

df = pd.read_excel("SWYNEX_Titanic_Data_Cleaned.xlsx")

print(df)