import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from collections import Counter

# importing csv
df=pd.read_csv("netflix_titles.csv")
# print (df)
# print(df.columns)
# for col in df.columns:
#     print(col)

print(list(df.columns.values))

# # cleaning data
# print(df.isnull().sum())
# df.fillna("unknown", inplace=True)
# df["release_year"] = pd.to_numeric (df["release_year"],errors="coerce")

# # data analysis and visualization
# sn.countplot(data=df, x="type" , hue="type", palette="coolwarm")
# plt.title("count of movies vs shows")
# plt.show()

# # top countries
# top_countries = df["country"].value_counts().head(5)
# top_countries.plot(kind="bar", color="skyblue")  
# plt.title("Top 10 Countries with Most Netflix Content")  
# plt.ylabel("Number of Titles")  
# plt.show()

# # popular genres
# genres = df["listed_in"].str.split(",").explode()  
# top_genres = Counter(genres).most_common(5)  
# genres_df = pd.DataFrame(top_genres, columns=["Genre", "Count"])  
# sn.barplot(data=genres_df, x="Count", y="Genre", palette="viridis")  
# plt.title("Most Common Netflix Genres")  
# plt.show()


# # popular directors
# pop_directors=df["director"].value_counts().head(5)
# pop_directors.plot(kind="bar", color="turquoise")
# plt.title("top 5 popular directors")
# plt.ylabel("number of movies")
# plt.show()