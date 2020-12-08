#How to Apply Lambda Functions  DataFrames_insert columns_ perform operation

import pandas as pd

#pd.__version__

#example 0:
d = {"val":[123,6,8]}
df = pd.DataFrame(d)
print(df)

#example 1:
a = {"values":[123,6,8]}
df1 = pd.DataFrame(a)
a=df1.apply(lambda x: x +100)
print(a)

#example 2: INSERTING  a new column to the data frame

b = {"values":[123,18,10]}
df2 = pd.DataFrame(b)
print(df2)

df2["Deflection"] =4
print(df2)



#example 3: INSERTING a new column to the data frame with string 

c = {"Beam Vertical Deflection":[25,23,29,28,25,30]}
df3 = pd.DataFrame(c)
print(df3)

df3["Residual Deflection"] =str("2mm")
print(df3)

#examplE 4: PERFORMING  operations between columns: example: Summation

b = {"Denomination":[str("Beam650"),str("Beam550"),str("Beam750")]}
df4 = pd.DataFrame(b)
print(df4)

df4["Beam Vertical Deflection"] =16
print(df4)

df4["Total Deflection"]=df4.apply(lambda x: x["Beam Vertical Deflection"] +9,axis =1)   # 9 mm : Dead Load
print(df4)
