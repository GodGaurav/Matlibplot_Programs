import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

for n in columns:
  #print(n)
  sns.countplot(df[n], order = df[n].value_counts().index)
  plt.xticks(rotation=30, fontsize = 10)
  plt.xlabel(columns, fontsize = 12)
  plt.title("{} Value Counts".format(n))
  plt.show()
  plt.clf()

