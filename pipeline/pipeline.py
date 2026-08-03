import sys
import pandas as pd


month = int(sys.argv[1])

df = pd.DataFrame({'day':[1,2], 'number_of_passanger':[3,4]})
df['month'] = month
print(df.head())

df.to_parquet(f'output_{month}.parquet') 


print(f'arguments, month-{month}')