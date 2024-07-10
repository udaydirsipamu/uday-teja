import pandas as pd
df=pd.read_csv("Emp.csv")
#print(df)
#print("no of rows:",len(df))
#print("Unique values in dept:",df['Dname'].unique())
#print("total no of depts:",df['Dname'].nunique())
#print(df.dropna())
#df['Dname']=df['Dname'].fillna("Marketing")
#print(df)
#for i in df.index:
 #   if df.loc[i,"Sal"] > 21000:
 #       df.loc[i,"Sal"]=195000
#print(df)
#for i in df.index:
#   if df.loc[i,"Ename"].startswith("A"):
#     print(df.loc[i,"Ename"])
#for i in df.index:
#   if df.loc[i,"Sal"] > 18000:
#       print(df.loc[i,"Ename"]," = ",df.loc[i,"Sal"])
#print("Highest sal:",df["Sal"].max())
#c
#df1=df[df["Sal"] == h]
#print(df1["Ename"])
#df_sorted=df.sort_values(by="Sal",ascending=False)
#sh=df_sorted["Sal"].unique()[1]
#df1=df[df["Sal"]==sh]
#print(df1['Ename'])
#print(sh)
#print(df[df["Sal"]>18000].shape[0]) or
#print(len(df[df["Sal"]>18000])) or
#print(df[df["Sal"]<=18000])
#for i in df.index:
#   if df.loc[i,"Sal"] > 18000:
#        df.drop(i,inplace=True)
#print(df)
#print(df.groupby("Dname").size())
#print(df["Dname"].value_counts())
#print(df.drop_duplicates())