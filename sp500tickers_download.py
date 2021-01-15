import pandas as pd


table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df.to_csv('SP500.csv')
df.to_csv('SP500-symbols.csv', columns=['Symbol'],index=False)

with open("SP500-symbols.csv")