import pandas as pd
df=pd.read_csv("Account.csv")
#print(df)
#df_sorted=df.sort_values(by="Bal")
#sh=df_sorted["Bal"].unique()[2]
#df1=df[df["Bal"]==sh]
#print(df1['Name'].unique())
#print(sh)
#print(df.sort_values(by="Name"))
#print("No of acc holders of each type\n",df["Type_acc"].value_counts())
#print("No of acc holders",df[df["Type_acc"]=="Saving"].shape[0])
#df1=df['Type_acc']=='Current'
#df.loc[df1,'Bal'] *=1.1
#print(df)
#for i in df.index:
#  if df.loc[i,"Name"].startswith("A") and df.loc[i,"Name"].endswith("r"):
#    df.drop(i,inplace=True)
#print(df)
#print("Unique names",df["Name"].unique)
df1=df[(df["Bal"]<10000) & (df["Type_acc"]=="Current")]
print(df1)
print(df)