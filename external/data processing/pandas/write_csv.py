import pandas as pd
data={
    'name':['Achyuth','Lekshmi','Abhishek','Nandu','Adithya','Alen','Athul'],
    'age':[21,21,21,22,23,23,21],
    'dept':["CS","CS","EC","CS","CS","EC","MECH"]
}
df=pd.DataFrame(data)
df.to_csv('details.csv',index=True)