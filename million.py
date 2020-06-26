import pandas as pd
import re
    # 1. Load the data and load chunks at the time!!!
#df= pd.read_csv("1000000 Sales Records.csv")
df=pd.read_csv("1000000 Sales Records.csv")

    # 2. Print the data to the console
#print(df)
pd.set_option('max_columns', None)
print(df)
#print (df.head(10))
#print (df.tail(10))

    # 3. Read The Columns
#print (df.columns)

    # 4. Read a spesific Conumn
#print(df["Units Sold"][0:10])
#print(df[["Units Sold","Region","Total Profit"]][0:10])

    # 5. Read a spesific Line
#print(df.iloc[0:10])

    # 6. Grab a spesific Location-Marocco
#print(df.iloc[1,1])

    # 7.Read  every row
# for i, j in df.iterrows():
#     if i<=10:
#         print(i,j["Unit Cost"])
    # 8. Find a Row which includes the word and print everything out..!
#print(df.loc[df["Country"]=="Greece"])

    # 9. generic high level stats
# #print(df. describe())

    # 10. Sorting by name
#print(df.sort_values("Total Cost").head(10))
#print(df.sort_values("Total Cost",ascending=False))

    # 11. Making Changes: adding a new column subtracting 2 values in the end of the list
# print (df.head(10))
# df["Unit Revenue"]=df["Unit Price"]-df["Unit Cost"]

    # 12. Drop a column
#df.drop(columns=["Total Cost"])

    # 13. Making Changes: adding a new column subtracting 2 values in the end of the list
    # and modifing the column order!!
# df["Unit rev"]=df.iloc[:,9:10].sum(axis=1)
# cols=list(df.columns.values)
# df=df[cols[9:10]+[cols[-1]]+cols[4:12]]
# print (df.head(10))

    # 14. Save the new CSV oe excel or something else..
# new=df.head(100)
# new.to_csv("modified.csv",index=False)

    # 15. Sellect a specific column
# print (df.head(10))
# print(df.loc[df["Unit Cost"]==6.92])

    # 16. Sellect a row with multiple conditions
# print(df.loc[(df["Unit Cost"]==6.92) & (df["Total Revenue"]==14862.69)])
# print(df.loc[(df["Unit Cost"]==6.92) | (df[" Total Revenue"]==14862.69)])
#print(df.loc[(df["Unit Cost"]==6.92) & (df["Total Revenue"]==14862.69) & (df["Order ID"]>399911630)])

    # 17. reset index and drop the old one
# new_df=df.loc[(df["Unit Cost"]==6.92) & (df["Total Revenue"]==14862.69) & (df["Order ID"]>399911630)]
# print(new_df.reset_index(drop=True))

    # 18. regular expresions- countains "south" in Country ignore the capilisation-filtering
#print (df.head(10))
#print(df.loc[df["Country"].str.contains("south",flags=re.I,regex=True)])

    # 19. filtering- find in Country colum countries they start with su on their name
#print(df.loc[df["Country"].str.contains("^su[a-z]",flags=re.I,regex=True)])

    # 20. Change the name of a column
# df.loc[df["Country"]=="Morocco", "Country"]="Maro"
# print(df["Country"])

    # 21. change the value of a cell acording to one requirement
# print(df)
# df.loc[df["Unit Price"]>100,["Unit Cost"]]='whatever'
# print(df)

    # 22. Group by Function group by country and see where we has the most sales

#print(df.groupby(["Country"]).mean().sort_values("Units Sold", ascending=False))

    # 23. Count how many inputs of each country we have
#print(df.groupby(["Country"]).count())
#print(df.groupby(["Country"]).count()["Total Cost"])


