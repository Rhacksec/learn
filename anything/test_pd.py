import pandas as pd

tables = pd.read_html("http://foxtools.ru/Proxy")

print(tables[0])